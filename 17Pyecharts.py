from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
#创建一个折线图对象
line = Line()
#添加xy数据
line.add_xaxis(['China','United States','United Kindom'])
line.add_yaxis("GDP",[30,20,10])

line.set_global_opts(
    title_opts=TitleOpts(title='show GDP',pos_left='center',pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)

line.render()#生成了一个render.html文件，将其拖拽到浏览器中进行查看