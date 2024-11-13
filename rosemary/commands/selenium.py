import os
import subprocess
import click


@click.command('selenium', help="Executes Selenium tests based on the environment.")
@click.argument('module', required=False)
def selenium(module):
    # Absolute paths
    working_dir = os.getenv('WORKING_DIR', '')
    modules_dir = os.path.join(working_dir, 'app/modules')

    def validate_module(module):
        """Check if the module exists."""
        if module:
            module_path = os.path.join(modules_dir, module)
            if not os.path.exists(module_path):
                raise click.UsageError(f"Module '{module}' does not exist.")
            selenium_test_path = os.path.join(module_path, 'tests', 'test_selenium.py')
            if not os.path.exists(selenium_test_path):
                raise click.UsageError(
                    f"Selenium test for module '{module}' does not exist at path "
                    f"'{selenium_test_path}'."
                )

    def run_selenium_tests_in_local(module):
        """Run the Selenium tests."""
        if module:
            selenium_test_path = os.path.join(modules_dir, module, 'tests', 'test_selenium.py')
            test_command = ['python', selenium_test_path]
        else:
            selenium_test_paths = []
            for module in os.listdir(modules_dir):
                tests_dir = os.path.join(modules_dir, module, 'tests')
                selenium_test_path = os.path.join(tests_dir, 'test_selenium.py')
                if os.path.exists(selenium_test_path):
                    selenium_test_paths.append(selenium_test_path)
            test_command = ['python'] + selenium_test_paths

        click.echo(f"Running Selenium tests with command: {' '.join(test_command)}")
        subprocess.run(test_command, check=True)

    # Validate module if provided
    if module:
        validate_module(module)

    if working_dir == '/app/':

        click.echo("Starting Selenium in Docker environment on port 4444")

        build_command = [
            "docker", "run", "-d", "-p", "4444:4444", "--name", "selenium_uvlhub_docker", "-v",
            "/dev/shm:/dev/shm", "selenium/standalone-chrome"]

        click.echo(f"Build command: {' '.join(build_command)}")
        subprocess.run(build_command, check=True)

        input()

        run_selenium_tests_in_local(module)

        click.echo("Stoping Selenium in Docker")

        stop_command = [
            "docker", "stop", "selenium_uvlhub_docker"]

        click.echo(f"Stop command: {' '.join(stop_command)}")
        subprocess.run(stop_command, check=True)

        click.echo("Removing Selenium in Docker")

        remove_command = [
            "docker", "rm", "selenium_uvlhub_docker"]

        click.echo(f"Remove command: {' '.join(remove_command)}")
        subprocess.run(remove_command, check=True)

        """     
        click.echo(click.style(
            "Currently it is not possible to run this "
            "command from a Docker environment, do you want to implement it yourself? ^^",
            fg='red'
        ))
        """

    elif working_dir == '':
        run_selenium_tests_in_local(module)

    elif working_dir == '/vagrant/':

        click.echo(click.style(
            "Currently it is not possible to run this "
            "command from a Vagrant environment, do you want to implement it yourself? ^^",
            fg='red'
        ))

    else:
        click.echo(click.style(f"Unrecognized WORKING_DIR: {working_dir}", fg='red'))
