from module_sample_api.configurations.app_conf import AppConf
from fastapi.responses import FileResponse


# [그룹 서비스]
# (루트 경로)
async def get_root(request):
    return AppConf.jinja2Templates.TemplateResponse(
        "home_page/home_page.html",
        {
            "request": request,
            "viewModel": {
                "homeTitle": AppConf.server_name,
                "env": AppConf.server_profile,
                "showApiDocumentBtn": AppConf.swagger_docs_enable
            }
        }
    )


# ----
# (/favicon.ico)
async def get_favicon():
    return FileResponse(f"{AppConf.module_folder_path}/z_resources/static/favicon.ico")
