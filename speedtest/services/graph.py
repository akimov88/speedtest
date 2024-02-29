import plotly.graph_objs as go


def figures(qs) -> tuple:
    download_figure, upload_figure = go.Figure(), go.Figure()
    download_figure.add_trace(
        go.Scatter(
            x=[result.timestamp for result in qs],
            y=[result.download_speed for result in qs],
        )
    )
    download_figure.update_layout(
        title='Download',
        xaxis_title='timestamp',
        yaxis_title='mb/s',
    )
    upload_figure.add_trace(
        go.Scatter(
            x=[result.timestamp for result in qs],
            y=[result.upload_speed for result in qs]
        )
    )
    upload_figure.update_layout(
        title='Upload',
        xaxis_title='timestamp',
        yaxis_title='mb/s',
    )
    return download_figure.to_html(), upload_figure.to_html()
