import pkg_resources

packages = pkg_resources.working_set
package_dict = {package.key: package.version for package in packages}

# SQLAlchemy와 관련된 패키지 정보 출력
for key, value in package_dict.items():
    if "sqlalchemy" in key.lower():
        print(f"{key}=={value}")
