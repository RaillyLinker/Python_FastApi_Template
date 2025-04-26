import module_sample_sql_alchemy.configurations.app_conf as app_conf
from fastapi.responses import FileResponse
from fastapi import Request, Response


# [그룹 서비스]
# (루트 경로)
async def get_root(
        request: Request,
        response: Response
):
    return app_conf.jinja2Templates.TemplateResponse(
        "home_page/home_page.html",
        {
            "request": request,
            "viewModel": {
                "homeTitle": app_conf.server_name,
                "env": app_conf.server_profile,
                "showApiDocumentBtn": app_conf.swagger_docs_enable
            }
        }
    )


# ----
# (/favicon.ico)
async def get_favicon(
        request: Request,
        response: Response
):
    return FileResponse(f"{app_conf.module_folder_path}/z_resources/static/favicon.ico")
