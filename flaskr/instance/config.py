"""
!这里用来弥补app.config.from_mapping()，无法映射到的缺省配置。
!也可以直接这里写配置，然后app.config.from_pyfile("config.py")，也行
"""
SECRET_KEY = 'dev'
