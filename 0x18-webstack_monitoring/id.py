#!/usr/bin/python3
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.models import *

# Set up your Datadog API and App keys
configuration = Configuration()
configuration.api_key['apiKeyAuth'] = '69c57d19f933de039aac5e3e480614ce'
configuration.api_key['appKeyAuth'] = '6e86ab367ab5e7f8cd45da23820e4cea89b18ddc'

# Initialize API client
with ApiClient(configuration) as api_client:
    dashboards_api = DashboardsApi(api_client)
    
    # Get the list of all dashboards
    response = dashboards_api.list_dashboards()

    # Print dashboard IDs and titles
    for dashboard in response.dashboards:
        print(f"Dashboard ID: {dashboard.id}, Title: {dashboard.title}")


