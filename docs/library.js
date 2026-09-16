'use strict';
function matches(report, filters) {
  const query = filters.query.trim().toLowerCase();
  return (!query || `${report.title} ${report.id}`.toLowerCase().includes(query)) &&
    ['task', 'year', 'role'].every(key => !filters[key] || report[key] === filters[key]);
}
function csv(rows) {
  const keys = ['id', 'title', 'year', 'role', 'task', 'url', 'note'];
  const quote = value => {
    let s = String(value ?? '');
    if (/^[=+@\-\t\r]/.test(s)) s = "'" + s;
    return '"' + s.replaceAll('"', '""') + '"';
  };
  return '\ufeff' + [keys.join(','), ...rows.map(row => keys.map(k => quote(row[k])).join(','))].join('\r\n');
}
if (typeof module !== 'undefined') module.exports = {matches, csv};
if (typeof document !== 'undefined') (async () => {
  try {
    const response = await fetch('reports.json');
    if (!response.ok) throw new Error('Report data unavailable');
    const reports = await response.json();
    const form = document.getElementById('filters');
    const fields = ['query', 'task', 'year', 'role'];
    const controls = Object.fromEntries(fields.map(k => [k, document.getElementById(k)]));
    let selected = reports;
    const restore = () => {
      const params = new URLSearchParams(location.search);
      fields.forEach(k => { controls[k].value = params.get(k) || ''; });
    };
    function filter(updateURL = true) {
      const values = Object.fromEntries(fields.map(k => [k, controls[k].value]));
      selected = reports.filter(row => matches(row, values));
      const ids = new Set(selected.map(r => r.id));
      reports.forEach(r => { document.getElementById(r.id).hidden = !ids.has(r.id); });
      document.getElementById('count').textContent = `${selected.length} of ${reports.length} reports`;
      document.getElementById('empty').hidden = selected.length !== 0;
      if (updateURL) {
        const url = new URL(location.href); url.search = '';
        fields.forEach(k => { if (values[k]) url.searchParams.set(k, values[k]); });
        history.replaceState(null, '', url);
      }
    }
    form.addEventListener('submit', e => e.preventDefault());
    form.addEventListener('input', () => filter());
    form.addEventListener('reset', () => { fields.forEach(k => { controls[k].value = ''; }); filter(); });
    document.getElementById('export').addEventListener('click', () => {
      const url = URL.createObjectURL(new Blob([csv(selected)], {type: 'text/csv;charset=utf-8'}));
      const link = document.createElement('a'); link.href = url; link.download = 'drl4conbot-reports.csv';
      document.body.appendChild(link);
      link.click(); link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 60000);
    });
    window.addEventListener('popstate', () => { restore(); filter(false); });
    restore(); filter(false); form.hidden = false;
  } catch (error) {
    document.getElementById('count').textContent = 'Search could not load. All 136 reports remain available below.';
  }
})();
