# Hands-on 4
## Make sure a private API key can safely be used in an action
In order to protect a private API key from the public, but still being able to use it in a GitHub Workflow, you can follow the following steps:

1. Go to the repository settings by clicking the "Settings" button in the ribbon on top of the page. Make sure you're browsing the repository.
2. Click "Secrets and variables". Choose "Actions" from the menu that pops up.
3. Click the green button that says "New repository secret".
4. Provide `WEATHER_API_KEY` as name and paste the API key value in the textbox underneath the "Secret" title.
5. Click the green "Add secret" button.
6. Update the workflow file such that it uses this secret. Check [this file](https://github.com/pverscha/actions_workshop_solutions/blob/main/.github/workflows/print_temperature_secret_city.yml) for the end result.
