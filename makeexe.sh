echo "*** Create Executable ***"
pyinstaller -y -w main.py

echo "Copying resources to dist folder"
cp piet.ico ./dist/main
cp ./gui/*.qrc ./dist/main
echo "[*] Done"