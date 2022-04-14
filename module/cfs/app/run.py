import minium

from config import log


class AppTest(minium.MiniTest):
    def test_get_all_pages_path(self):
        self.app.redirect_to("/pages/home/home/index")
        self.page.get_element("view.search-box[text(contains(\"查询科普\"))]").click()
        self.page.get_element("input.search-box[text(contains(\"搜索疾病/问题\"))]").input("心血管")
        self.page.get_element("view.text-msg >>> rich-text", inner_text="测试患教资料").click()
