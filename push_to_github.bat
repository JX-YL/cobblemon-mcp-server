@echo off
chcp 65001 >nul
echo.
echo ========================================
echo   强制推送 v1.3.0 到 GitHub
echo ========================================
echo.
echo 正在推送...
git push -f origin main
echo.
echo 删除远程 v1.4.0 标签...
git push origin :refs/tags/v1.4.0
echo.
echo ========================================
echo   完成！请检查 GitHub Release 页面
echo   删除 v1.4.0 Release
echo ========================================
echo.
pause

