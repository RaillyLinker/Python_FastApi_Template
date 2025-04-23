from module_sample_api.configurations.app_conf import AppConf


# [그룹 서비스]
# (루트 경로)
async def get_root(request):
    return AppConf.jinja2Templates.TemplateResponse(
        "index.html",
        {"request": request, "message": "Hello from FastAPI!"}
    )
