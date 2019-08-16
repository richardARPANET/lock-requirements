from pypi_simple import PyPISimple

from .parser import parse


def lock(requirements_path, endpoint):
    return _lock_requirements(
        input_path=requirements_path,
        output_path=requirements_path,
        endpoint=endpoint,
    )


def _lock_requirements(*, input_path, output_path, endpoint):
    output_lines = []
    with open(input_path, 'r') as file_:
        for req in parse(file_):
            if isinstance(req, str):
                output_lines.append(f'{req}\n')
            elif req.uri:
                output_lines.append(f'{req.line}\n')
            else:
                _, version = _get_latest_versions(
                    package_name=req.name, endpoint=endpoint
                )
                extras = sorted(req.extras)
                extras_str = f'[{",".join(extras)}]' if extras else ''
                if version is None:
                    output_lines.append(f'{req.name}{extras_str}\n')
                else:
                    output_lines.append(f'{req.name}{extras_str}=={version}\n')

    with open(output_path, 'w') as file_:
        for line in output_lines:
            file_.write(line)
    return output_path


def _get_latest_versions(*, package_name, endpoint):
    pypi = PyPISimple(endpoint=endpoint)
    packages = pypi.get_project_files(package_name)
    try:
        latest_version = packages[-1].version
    except IndexError:
        # Package not found
        latest_version = None
    return (package_name, latest_version)
