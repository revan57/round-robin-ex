from starlette.applications import Starlette
from starlette.responses import RedirectResponse, HTMLResponse
from starlette.routing import Route

from app.service import get_video_node


async def get_video(request):
    redirect_url = get_video_node(request)
    if redirect_url:
        return RedirectResponse(redirect_url)
    else:
        return HTMLResponse('404 Not found.', 404)

app = Starlette(debug=True, routes=[
    Route('/', get_video),
])
