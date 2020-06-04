from core.node_queue import NodeQueue
from urllib import parse


def get_video_node(request):
    if request.query_params.get('video'):
        parsed_url = parse.urlparse(str(request.query_params['video']))
        if parsed_url.scheme and parsed_url.netloc:
            q = NodeQueue()
            node = q.get_node()
            node = parsed_url.netloc if node == 'origin' else node

            return f"{parsed_url.scheme}://{node}{parsed_url.path}"
