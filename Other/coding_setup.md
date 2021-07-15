# My Coding Setup

I've used a lot of different setups for data science and it changes all the time. This is just a quick little list in case someone (myself included) needs to look at it.

- Use VSCode to write most major code (including Jupyter Notebooks)
- Attempt to use Git repositories to maintain versioning of projects. (You can sync overleaf with git btw)
- Use Dropbox to sync everything (including the git clones)
- Dracula colour for everything



# Tech installs:
## oh-my-zsh
plugins=(
	git
	zsh-syntax-highlighting
	zsh-autosuggestions
	virtualenv
)

alias l='ls -Alhgo'
alias G='| grep -i'
alias ip="curl icanhazip.com"

# Python
I'm sick of dealing with the whole of anaconda but also agree that conda can be somewhat useful. The current compromise is to use **miniforge** to install a conda python installation and use pip from then onwards.


# Homebrew Installs
### brews
imagemagick
node

### casks
appcleaner
jupyter-notebook-viewer
sublime-text
gimp
iterm2
code

# Latex
* Use VScode and the Latex Workshop extention to compile your $\Latex$. This exention doesn't alwasy work so be prepared to `latexmk -cd -f -pdf -synctex=1 -interaction=nonstopmode %DOC%` in case of emergency. 
* Install `texlive` [*without*](https://tex.stackexchange.com/questions/397174/minimal-texlive-installation*) any docs, sourcecode or extra packages. You will need to manually install many packages. Use `sudo tlmgr install pkg ` or `sudo texliveonfly --compiler=latexmk --arguments='-pdf' %DOC%`.
* If you want to collarborate or just have a backup. Create a project on Overleaf and git clone it to your local. This git instance is store on overleaf with versioning. You will always be able to use Overleaf to complie in future. Dropbox will sync locally.



# Apps to not forget

Sometimes you get a new laptop and need to remember all those apps you love.

* Alfred: For search, snippets, and workflows. I live off this. Preferences synced in dropbox.

* Journey: For journally (it's free and syncs with Drive)
* Mathpix Snipping Tool: For converting images to latex
* Notability: For handwritten drafting and reviewing. 
*  Zoom, Teams: Don't forget to allow the privacy.
* Amphetamine: Keep your computer awake
* Magnet: Window hotkey layout.
* Zotero: Paper Management
* Cyberduck: Connecting to servers
  
