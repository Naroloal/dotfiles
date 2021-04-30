"""""""""Basic configuration""""""""""""
set relativenumber
set number
set mouse=a
"Mapleader"
:let mapleader = "," 

nmap <leader>n :bnext
nmap <C-j> <C-w>j
nmap <C-k> <C-w>k
tnoremap <Esc> <C-\><C-n>
""""""""""""""""""""""""""""""""""""""""

""""""""""""""PLUGINS"""""""""""""""""""
call plug#begin()
Plug 'junegunn/vim-easy-align' "Aligner
Plug 'cometsong/CommentFrame.vim' 
Plug 'vim-airline/vim-airline'
"Plug 'davidhalter/jedi-vim'
"Plug 'zchee/deoplete-jedi'
Plug 'kiteco/vim-plugin'
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'scrooloose/nerdcommenter'
Plug 'kassio/neoterm'
call plug#end()

""""""""""""""""""""""""""""""""""""""""


"Plugins configuration"
" Start interactive EasyAlign in visual mode (e.g. vipga)
xmap ga <Plug>(EasyAlign)
" Start interactive EasyAlign for a motion/text object (e.g. gaip)
nmap ga <Plug>(EasyAlign)

"let g:deoplete#enable_at_startup = 1
"inoremap <expr><tab> pumvisible() ? "\<c-n>" : "\<tab>"
"autocmd InsertLeave,CompleteDone * if pumvisible() == 0 | pclose | endif
"" disable autocompletion, because we use deoplete for completion
"let g:jedi#completions_enabled = 0
"" open the go-to function in split, not another buffer
"let g:jedi#use_splits_not_buffers = "right"

let g:neoterm_default_mod='belowright' " open terminal in bottom split
let g:neoterm_size=16 " terminal split size
let g:neoterm_autoscroll=1 " scroll to the bottom when running a command
let g:neoterm_autojump=1
nnoremap <leader><F9> :TREPLSendLine<cr>j " send current line and move down
vnoremap <leader><F9> :TREPLSendSelection<cr> " send current selection
nnoremap <leader><F5> :TREPLSendFile<Enter>i<Enter>
nnoremap <leader>tl :<c-u>exec v:count.'Tclear'<cr>
