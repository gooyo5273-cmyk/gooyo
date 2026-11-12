#!/usr/bin/env python3
"""src/app.html + SheetJS + 관리 품번 리스트 -> 단일 HTML 파일로 묶는다.
사용법: python3 build.py"""
import json, pathlib
root = pathlib.Path(__file__).parent
html = (root / "src/app.html").read_text(encoding="utf-8")
lib = (root / "vendor/xlsx.full.min.js").read_text(encoding="utf-8").replace("</script", "<\\/script")
master = json.dumps(json.loads((root / "src/master.json").read_text(encoding="utf-8")), ensure_ascii=False, separators=(",", ":"))
assert "/*__XLSX__*/" in html and "/*__MASTER__*/" in html
html = html.replace("/*__XLSX__*/", lib).replace("/*__MASTER__*/", master)
out = root / "주조_생산실적_분석.html"
out.write_text(html, encoding="utf-8")
print("built", out, f"{out.stat().st_size/1024:.0f} KB")
