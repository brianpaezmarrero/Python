SELECT clients.first_name, clients.last_name,billing.amount, billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id;

SELECT sites.domain_name,leads.first_name,leads.last_name
FROM sites
JOIN leads ON sites.id = leads.sites_id;

SELECT clients.first_name, clients.last_name, sites.domain_name, leads.first_name
FROM clients
JOIN sites ON clients_id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id 