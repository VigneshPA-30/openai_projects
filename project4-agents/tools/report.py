from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel


def write_report(filename, html):
    if not filename.endswith('.html'):
        filename = filename + '.html'
    with open(filename, "w") as f:
        f.write(html)


class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str

write_report_tool = StructuredTool.from_function(
    func=write_report,
    name="write_report",
    description="Used for writing reports as an html file.",
    args_schema=WriteReportArgsSchema
)