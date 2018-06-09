lc-spider -c solutions/config.json
npm run generate
rm -f README.md
cp ./solutions/README.md ./
git add .
git commit -m "add my solutions"
git push origin master