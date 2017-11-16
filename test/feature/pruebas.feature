Feature: Go to odoo
Scenario: Visit odoo
		Given: I go to "http:0.0.0.0:8069"
		Then: I should see the field with id "login" 