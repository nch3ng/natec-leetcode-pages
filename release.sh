rm -f README.md
lc-spider -c solutions/config.json
npm run generate
git add .
git commit -m "add my solutions"
git push origin master