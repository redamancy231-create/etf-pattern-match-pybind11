Reading prompt from stdin...
OpenAI Codex v0.144.1
--------
workdir: C:\Users\33455
model: gpt-5.6-sol
provider: packycode
approval: never
sandbox: danger-full-access
reasoning effort: xhigh
reasoning summaries: none
session id: 019f6f6c-7965-7c13-abbc-2427888e23e2
--------
user
You are adding C++ native tests for the "etf-pattern-match-pybind11" project. Source code is at: E:/workspace/projects/形态匹配ETF策略-pybind11

Read the C++ source file src/cpp/etf_core.cpp to understand the 8 core functions, then implement the following.

## Task: Add doctest-based C++ native tests

### What to create

1. **`tests/test_etf_core.cpp`** — doctest test file with tests for all 8 C++ functions:

   Required test cases for each function:
   - empty input (return value, no crash)
   - single-element input
   - NaN/Inf inputs (verify policy: rejection or propagation)
   - extreme values (very large/small numbers)
   - known-answer case (compute expected result by hand or from existing Python verify script)
   - For DTW: tie behavior, boundary window behavior
   - For pattern_match_single: invalid T_idx (out of bounds)

2. **`tests/CMakeLists.txt`** — CMake config for building and running the test:
   - Link against doctest (header-only, download or use FetchContent)
   - Link against the existing etf_core library
   - Add a `test_native` target

### Requirements

- Use `doctest` framework
- Test algorithmic correctness, not Python binding layer (that's tested elsewhere)
- Document the expected NaN/Inf policy explicitly in comments
- Include provenance comment: "GPT-5.6-Sol (via Codex CLI), 2026-07-17"
- Match existing code style (C++20, same includes/conventions as etf_core.cpp)

### What NOT to do

- Don't modify etf_core.cpp or CMakeLists.txt in project root
- Don't run the tests
- Don't add Python test files

### Output

Write the complete new files.

warning: Skill descriptions were shortened to fit the 2% skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
2026-07-17T09:33:57.953194Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when Client(HttpRequest(HttpRequest("http/request failed: error sending request for url (https://developers.openai.com/mcp)")))
  → Inspect project instructions, CMake structure, headers, and src/cpp/etf_core.cpp
  • Design comprehensive doctest cases for all eight core functions
  • Create tests/test_etf_core.cpp and tests/CMakeLists.txt without modifying existing files
  • Review new files statically for API/style/CMake correctness (do not run tests)
2026-07-17T09:34:08.296201Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when Client(HttpRequest(HttpRequest("http/request failed: error sending request for url (https://developers.openai.com/mcp)")))
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Get-ChildItem -Force; Write-Host '"'--- parent/project AGENTS files ---'; Get-ChildItem -Path 'E:\\workspace\\projects' -Filter AGENTS.md -Force -ErrorAction SilentlyContinue; Get-ChildItem -Path 'E:\\workspace\\projects\\形态匹配ETF策略-pybind11' -Filter AGENTS.md -Recurse -Force -ErrorAction SilentlyContinue | Select-Object FullName; Write-Host '--- project root ---'; Get-ChildItem -LiteralPath 'E:\\workspace\\projects\\形态匹配ETF策略-pybind11' -Force" in C:\Users\33455
 succeeded in 515ms:


    目录: C:\Users\33455


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d-----         2026/5/31      1:20                .adal                                                                
d-----          2026/4/7     17:02                .agents                                                              
d-----         2026/5/31      1:20                .aider-desk                                                          
d-----          2025/6/1     18:19                .AivmVbox                                                            
d-----         2026/6/25     14:52                .anaconda                                                            
d-----        2024/11/27     12:58                .android                                                             
d-----         2026/5/31      1:20                .augment                                                             
d-----          2026/5/4      1:26                .aws                                                                 
d-----          2026/5/4      1:26                .azure                                                               
d-----         2026/5/31      1:21                .bailian                                                             
d-----         2026/5/31      1:20                .bob                                                                 
d-----         2026/4/29     20:52                .bun                                                                 
d-----         2026/5/11     15:29                .cache                                                               
d-----          2026/5/4      1:29                .cagent                                                              
d-----         2026/7/14      0:33                .cc-switch                                                           
d-----          2026/5/3     21:41                .cherrystudio                                                        
d-----         2026/7/17     17:33                .claude                                                              
d-----         2026/5/31      1:20                .codeartsdoer                                                        
d-----         2026/5/31      1:20                .codebuddy                                                           
d-----         2026/5/31      1:20                .codeium                                                             
d-----         2026/5/31      1:20                .codemaker                                                           
d-----         2026/5/31      1:20                .codestudio                                                          
d-----         2026/7/17     17:33                .codex                                                               
d-----         2026/5/31      1:20                .commandcode                                                         
d-----         2026/6/25     15:00                .conda                                                               
d-----         2026/7/17      0:33                .config                                                              
d-----        2024/12/31     18:39                .configverge                                                         
d-----         2026/5/31      1:20                .continue                                                            
d-----         2026/6/25     14:56                .continuum                                                           
d-----         2026/5/11      0:31                .copilot                                                             
d-----         2026/7/14     18:14                .DataTool                                                            
d-----         2026/6/20     23:21                .dbus-keyrings                                                       
d-----         2026/3/29     18:52                .DMMGAMEPLAYERSDK                                                    
d-----         2026/5/18     23:37                .docker                                                              
d-----          2026/7/2     13:59                .dotnet                                                              
d-----         2026/5/31      1:20                .factory                                                             
d-----         2026/5/31      1:20                .forge                                                               
d-----         2026/5/19     17:59                .goldminer3                                                          
d-----         2026/6/13     17:52                .headroom                                                            
d-----         2026/5/31     13:51                .hermes                                                              
d-----         2025/4/12     20:05                .idlerc                                                              
d-----         2026/5/31      1:20                .iflow                                                               
d-----         2024/7/29     18:12                .insomniac                                                           
d-----         2025/11/5     18:12                .ipython                                                             
d-----         2026/5/31      1:20                .junie                                                               
d-----         2026/7/12     13:13                .jupyter                                                             
d-----         2026/5/31      1:20                .kilocode                                                            
d-----         2026/7/17      0:20                .kimi                                                                
d-----         2026/7/17      0:24                .kimi-webbridge                                                      
d-----         2026/7/12      0:15                .kimi-work                                                           
d-----         2026/5/31      1:20                .kiro                                                                
d-----         2026/5/31      1:20                .kode                                                                
d-----         2025/2/21     13:04                .leigod                                                              
d-----         2026/5/10     23:05                .local                                                               
d-----         2025/11/5     18:12                .matplotlib                                                          
d----l          2026/6/1     12:31                .mavis                                                               
d-----         2026/5/31      1:20                .mcpjam                                                              
d-----         2026/6/27     16:30                .minimax                                                             
d-----          2026/6/1     12:30                .minimax-agent-cn                                                    
d-----         2026/5/11     15:29                .modelscope                                                          
d-----         2026/5/31      1:20                .mux                                                                 
d-----         2026/5/31      1:20                .neovate                                                             
d-----        2025/10/25     15:15                .nn-acc                                                              
d-----        2025/10/25     15:15                .nn-im                                                               
d-----          2026/7/2     13:59                .nuget                                                               
d-----          2026/5/1     19:06                .ollama                                                              
d-----         2026/5/31      1:20                .openclaw                                                            
d-----         2026/5/31      1:20                .openhands                                                           
d-----         2026/5/31      1:20                .pi                                                                  
d-----         2026/5/31      1:20                .pochi                                                               
d-----         2026/5/31      1:20                .qoder                                                               
d-----          2026/7/2     17:43                .qwen                                                                
d-----         2026/5/31      1:20                .roo                                                                 
d-----         2026/5/31      1:20                .rovodev                                                             
d-----         2026/5/31      1:20                .snowflake                                                           
d-----         2026/3/26     13:23                .spss                                                                
d-----        2025/12/24     12:42                .spyder-py3                                                          
d-----         2026/5/30     22:47                .ssh                                                                 
d-----         2026/2/15     19:57                .swt                                                                 
d-----         2026/5/31      1:20                .tabnine                                                             
d-----         2026/5/31      1:20                .trae                                                                
d-----         2026/5/31      1:20                .trae-cn                                                             
d-----         2026/5/31      1:20                .vibe                                                                
d-----        2025/10/22     20:16                .vscode                                                              
d-----          2026/5/1     16:16                .vscode-shared                                                       
d-----         2026/6/14     21:32                .zcode                                                               
d-----         2026/5/31      1:20                .zencoder                                                            
d-----         2023/6/17     10:45                ansel                                                                
d--h--         2025/2/25     21:22                AppData                                                              
d--hsl         2025/2/25     19:52                Application Data                                                     
d-----         2026/6/26     22:50                bin                                                                  
d-----         2026/7/16      0:37                Chess-for-EasyX-review                                               
d-r---         2025/2/25     21:26                Contacts                                                             
d--hsl         2025/2/25     19:52                Cookies                                                              
d-----          2025/2/6     16:50                Creative Cloud Files                                                 
d-----          2026/7/4     16:21                crosslink-updates                                                    
d-r---         2026/7/17     12:46                Desktop                                                              
d-r---         2026/7/12      0:15                Documents                                                            
d-----         2026/7/16      0:04                docx-pipeline                                                        
d-r---         2026/7/16     17:12                Downloads                                                            
d-----          2026/5/4      1:52                edict                                                                
d-r---         2025/2/25     21:26                Favorites                                                            
d-----         2026/7/15     23:59                independent-review-toolkit                                           
d-----          2026/7/4     17:08                issue-templates                                                      
d-----         2025/11/5     18:31                Jedi                                                                 
d-r---         2026/2/28     15:18                Links                                                                
d--hsl         2025/2/25     19:52                Local Settings                                                       
d-----         2026/7/16      0:04                ma-case-study-pipeline                                               
d-----          2026/7/9      0:15                MinerU                                                               
d-r---         2025/4/16     17:23                Music                                                                
d-----         2026/5/11     21:37                mx_output                                                            
d--hsl         2025/2/25     19:52                My Documents                                                         
d-----         2025/11/1     12:28                My PTE Files                                                         
d--hsl         2025/2/25     19:52                NetHood                                                              
dar--l          2023/8/4     13:28                OneDrive                                                             
d-r---         2026/5/10     20:11                Pictures                                                             
d-----         2026/5/11      0:13                ppt-master-main                                                      
d--hsl         2025/2/25     19:52                PrintHood                                                            
d-----         2026/5/19     18:59                projects                                                             
d-----         2026/7/16      0:03                prompt-tdd-methodology                                               
d-----         2026/7/12     16:48                prompts                                                              
d--hsl         2025/2/25     19:52                Recent                                                               
d-r---         2026/4/25     17:08                Saved Games                                                          
d-r---         2025/2/25     21:26                Searches                                                             
d--hsl         2025/2/25     19:52                SendTo                                                               
d-----          2026/7/2     13:57                source                                                               
d-----         2026/7/12     13:27                temp                                                                 
d--hsl         2025/2/25     19:52                Templates                                                            
d-----          2026/7/2     14:05                test_vs2026                                                          
d-----         2026/7/16      0:35                Twoplayersarchery-review                                             
d-r---         2025/6/13     13:26                Videos                                                               
d-----          2026/7/7     11:56                workspace                                                            
d--h--         2026/7/17     12:46                WPS Cloud Files                                                      
d-----         2026/4/19     15:09                WPSDrive                                                             
d-----         2026/4/22      9:46                xwechat_files                                                        
d-----         2026/6/14     21:28                ZCodeProject                                                         
d-----         2026/7/17     15:31                _review_docx_pipeline                                                
d-----         2026/7/17     15:42                _review_etf_pattern                                                  
d--hsl         2025/2/25     19:52                「开始」菜单                                                               
-a----         2026/7/16     23:41          21326 .bash_history                                                        
-a----         2026/7/17     17:31          11011 .claude.json                                                         
-a----         2026/6/25      0:30            352 .gitconfig                                                           
-a----         2025/10/1      0:49            853 .heyboxacc.conf                                                      
-a----         2026/3/24     16:55            123 .heybox_pc.conf                                                      
-a----         2026/6/30     15:39            166 .lsp.json                                                            
-a----         2026/7/17      0:37             81 .netease_mcp_device.json                                             
-a----         2026/6/19     20:33             40 .npmrc                                                               
-a----         2026/3/17      0:21           4187 .python_history                                                      
-a----         2026/6/18      2:28           2188 AGENTS.md                                                            
-a----         2026/7/12     15:57          23885 blob.b64                                                             
-a----          2026/6/6     15:45           1367 boot_diag.ps1                                                        
-a----          2026/6/6     15:46           1941 boot_diag2.ps1                                                       
-a----         2026/6/16     14:22          15138 build_comparison.py                                                  
-a----          2026/7/4     16:18           9671 claude-md-bilingual.md                                               
-a----          2026/7/1     17:50            933 clean_history.py                                                     
-a----          2026/7/1     17:53            876 clean_history_ptdd.py                                                
-a----         2026/6/20      3:15          23075 codex_crosscheck_prompt.txt                                          
-a----         2026/6/20      3:42          15789 codex_framework_consistency_prompt.txt                               
-a----         2026/6/20      3:24          71610 codex_retrospect_review_prompt.txt                                   
-a----         2026/6/20      3:37          10724 codex_spotcheck_prompt.txt                                           
-a----          2026/7/1     13:34           1536 count_cjk.py                                                         
-a----          2026/7/1     17:43           1909 desensitize_reviews.py                                               
-a----          2026/7/4     16:15           9456 etf-readme-bilingual.md                                              
-a----         2026/5/30     14:17           3953 fetch_all_data.py                                                    
-a----         2026/5/30     14:15           1014 fetch_financial_data.py                                              
-a----          2026/7/4     16:18           2772 file-index-bilingual.md                                              
-a----         2026/5/14     22:01          33233 gen_docx.js                                                          
-a----         2026/6/22     23:33          32286 glossary.json                                                        
-a----         2026/6/22     23:33          18812 glossary.md                                                          
-a----          2026/6/6     15:51           2120 hw_diag.ps1                                                          
-a----         2026/5/15      0:08           5837 md_to_docx.py                                                        
-a----         2026/6/18     13:00           5907 memory_slim_batch2_codex_crosscheck_prompt.md                        
-a----         2026/6/18     12:05            876 memory_slim_batch2_codex_lastmsg.txt                                 
-a----         2026/6/18     11:55           6377 memory_slim_batch2_codex_review_prompt.md                            
-a----         2026/6/18     13:09            606 memory_slim_batch2_crosscheck_lastmsg.txt                            
-a----         2026/5/26     17:47           6094 mx_data_301666上市以来每个交易日收盘价_涨跌幅.xlsx                                  
-a----         2026/5/26     17:47            487 mx_data_301666上市以来每个交易日收盘价_涨跌幅_description.txt                       
-a----         2026/5/26     17:47          11198 mx_data_301666公司简介_主营业务_所属行业_上市日期.xlsx                               
-a----         2026/5/26     17:47            676 mx_data_301666公司简介_主营业务_所属行业_上市日期_description.txt                    
-a----         2026/5/26     17:46           6439 mx_data_301666最新价_涨跌幅_换手率_量比_主力资金净流入.xlsx                            
-a----         2026/5/26     17:46            572 mx_data_301666最新价_涨跌幅_换手率_量比_主力资金净流入_description.txt                 
-a----         2026/5/26     17:46           6328 mx_data_301666近一年每个交易日收盘价_涨跌幅_成交量.xlsx                               
-a----         2026/5/26     17:46            523 mx_data_301666近一年每个交易日收盘价_涨跌幅_成交量_description.txt                    
-a----         2026/5/26     17:47           5335 mx_data_301666近一年每日收盘价.xlsx                                          
-a----         2026/5/26     17:47            369 mx_data_301666近一年每日收盘价_description.txt                               
-a----         2026/5/26     17:46          10251 mx_data_大普微(301666)基本信息_主营业务_所属行业_成立时间_总股本_流通股本.xlsx                 
-a----         2026/5/26     17:46            791 mx_data_大普微(301666)基本信息_主营业务_所属行业_成立时间_总股本_流通股本_description.txt      
-a----          2026/6/6     16:06           2215 nic_apply.ps1                                                        
-a----          2026/6/6     15:55            857 nic_diag.ps1                                                         
-a----          2026/6/6     19:07            540 nic_fix_result.txt                                                   
-a----          2026/6/6     16:05           1484 nic_preflight.ps1                                                    
-a-hs-        2023/12/26     16:15              0 ntuser-OP1703578504916.dat.LOG1                                      
-a-hs-        2023/12/26     16:15              0 ntuser-OP1703578504916.dat.LOG2                                      
-a-hs-          2024/1/1     17:40              0 ntuser-OP1704102005731.dat.LOG1                                      
-a-hs-          2024/1/1     17:40              0 ntuser-OP1704102005731.dat.LOG2                                      
-a-hs-          2024/1/4     10:15         131072 ntuser-OP1704334538363.dat.LOG1                                      
-a-hs-          2024/1/4     10:15              0 ntuser-OP1704334538363.dat.LOG2                                      
-a-hs-          2024/1/4     10:15          65536 ntuser-OP1704334538363.dat{a2332f18-cdbf-11ec-8680-002248483d79}.TM.b
                                                  lf                                                                   
-a-hs-          2024/1/4     10:15         524288 ntuser-OP1704334538363.dat{a2332f18-cdbf-11ec-8680-002248483d79}.TMCo
                                                  ntainer00000000000000000001.regtrans-ms                              
-a-hs-          2024/1/4     10:15         524288 ntuser-OP1704334538363.dat{a2332f18-cdbf-11ec-8680-002248483d79}.TMCo
                                                  ntainer00000000000000000002.regtrans-ms                              
-a-hs-         2024/1/11     11:54         167936 ntuser-OP1704945251780.dat.LOG1                                      
-a-hs-         2024/1/11     11:54              0 ntuser-OP1704945251780.dat.LOG2                                      
-a-hs-         2024/1/11     11:54          65536 ntuser-OP1704945251780.dat{a2332f18-cdbf-11ec-8680-002248483d79}.TM.b
                                                  lf                                                                   
-a-hs-         2024/1/11     11:54         524288 ntuser-OP1704945251780.dat{a2332f18-cdbf-11ec-8680-002248483d79}.TMCo
                                                  ntainer00000000000000000001.regtrans-ms                              
-a-hs-         2024/1/11     11:54         524288 ntuser-OP1704945251780.dat{a2332f18-cdbf-11ec-8680-002248483d79}.TMCo
                                                  ntainer00000000000000000002.regtrans-ms                              
-a-hs-         2024/1/22     16:35          98304 ntuser-OP1705912532043.dat.LOG1                                      
-a-hs-         2024/1/22     16:35              0 ntuser-OP1705912532043.dat.LOG2                                      
-a-hs-         2024/1/22     16:35          65536 ntuser-OP1705912532043.dat{a2332f18-cdbf-11ec-8680-002248483d79}.TM.b
                                                  lf                                                                   
-a-hs-         2024/1/22     16:35         524288 ntuser-OP1705912532043.dat{a2332f18-cdbf-11ec-8680-002248483d79}.TMCo
                                                  ntainer00000000000000000001.regtrans-ms                              
-a-hs-         2024/1/22     16:35         524288 ntuser-OP1705912532043.dat{a2332f18-cdbf-11ec-8680-002248483d79}.TMCo
                                                  ntainer00000000000000000002.regtrans-ms                              
-a-h--         2026/7/17     12:38       51642368 NTUSER.DAT                                                           
-a-hs-         2025/2/25     19:52        5242880 ntuser.dat.LOG1                                                      
-a-hs-         2025/2/25     19:52       12548096 ntuser.dat.LOG2                                                      
-a-hs-          2026/4/6     13:54          65536 NTUSER.DAT{6bc5a34f-f352-11ef-9b22-e073e7ec8bed}.TM.blf              
-a-hs-          2026/4/6     13:54         524288 NTUSER.DAT{6bc5a34f-f352-11ef-9b22-e073e7ec8bed}.TMContainer000000000
                                                  00000000001.regtrans-ms                                              
-a-hs-         2026/3/29      8:43         524288 NTUSER.DAT{6bc5a34f-f352-11ef-9b22-e073e7ec8bed}.TMContainer000000000
                                                  00000000002.regtrans-ms                                              
---hs-         2025/2/25     21:26             20 ntuser.ini                                                           
-a----         2026/6/14     18:21       41164800 pandoc-3.10-windows-x86_64.msi                                       
-a----         2026/7/12     16:01          16213 payload.json                                                         
-a----         2026/7/12     16:07          16647 payload2.json                                                        
-a----         2026/7/12     17:10          16800 payload_etf.json                                                     
-a----          2026/6/6     15:53           1637 pcie_map.ps1                                                         
-a----          2026/7/4     17:08           3241 project_status_updated.md                                            
-a----         2026/7/12     16:06          12377 readme_current.md                                                    
-a----         2026/7/12     17:10          12484 readme_etf.md                                                        
-a----         2026/7/12     15:58          12054 readme_fixed.md                                                      
-a----         2026/7/12     15:57          11921 readme_orig.md                                                       
-a----         2026/7/16      0:32           2766 review-result-archery.txt                                            
-a----          2025/9/7     18:06          88229 rpro.log                                                             
-a----          2026/5/4     12:51             48 sansheng.bat                                                         
-a----         2026/5/12     13:26           3003 skills-lock.json                                                     
-a----          2026/7/4     16:54          92707 social-preview.png                                                   
-a----         2026/6/30     15:23           2257 temp_codex_etf_review.txt                                            
-a----         2026/6/24     19:33           5587 temp_compare.py                                                      
-a----         2026/6/24     19:34           2522 temp_compare2.py                                                     
-a----         2026/6/24     19:34           1207 temp_compare3.py                                                     
-a----         2026/6/24     19:35           3200 temp_compare4.py                                                     
-a----         2026/6/24     19:35           2185 temp_compare5.py                                                     
-a----          2026/5/7     13:28           1672 tmp_stock_query.py                                                   
-a----         2026/5/11     15:27           1281 transcribe.py                                                        
-a----          2026/6/6     15:52           1487 whea_diag.ps1                                                        
-a----          2026/6/6     16:08           1612 whea_recheck.ps1                                                     
-a----         2026/5/30     14:21           1370 yjbb_000333.csv                                                      
-a----         2026/5/30     14:21           1353 yjbb_600019.csv                                                      
-a----         2026/5/30     14:21           1042 yjbb_601766.csv                                                      
-a----         2026/7/17     15:31          22333 _apply_docx_patch.py                                                 
-a----         2026/7/17     15:38           6978 _apply_etf_patch.py                                                  
-a----         2026/7/17     15:40           9809 _apply_etf_tests.py                                                  
-a----         2026/7/17     15:41           1431 _fix_etf_patch.py                                                    
-a----         2026/5/30     14:32          12521 公开渠道真实数据汇总.json                                                      
-a----         2026/5/30     14:23           5924 公开渠道真实数据汇总.md                                                        
-a----         2026/5/30     14:22           3802 整理公开数据.py                                                            
-a----         2026/5/30     14:30           7725 论文案例分析评价.json                                                        
-a----         2026/5/30     14:29           7675 论文案例分析评价.md                                                          
-a----         2026/5/30     14:21           3140 财务数据汇总.md                                                            
--- parent/project AGENTS files ---
--- project root ---


    目录: E:\workspace\projects\形态匹配ETF策略-pybind11


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d--h--         2026/7/17     15:01                .git                                                                 
d-----          2026/7/5     12:58                .github                                                              
d-----          2026/7/3     21:42                .pytest_cache                                                        
d-----         2026/7/16     17:17                benchmarks                                                           
d-----         2026/7/12     18:00                build                                                                
d-----         2026/7/12     19:56                docs                                                                 
d-----         2026/7/12     19:41                notebooks                                                            
d-----          2026/7/3     21:29                src                                                                  
d-----         2026/7/12     19:41                tests                                                                
d-----         2026/7/17     17:32                _review                                                              
d-----         2026/7/12     19:33                审查提示词                                                                
-a----          2026/7/4     14:22            397 .gitignore                                                           
-a----         2026/7/16     16:48           1434 CHANGELOG.md                                                         
-a----         2026/7/16     17:29            853 CITATION.cff                                                         
-a----         2026/7/12     19:55          12069 CLAUDE.md                                                            
-a----         2026/7/16     16:48           2653 CMakeLists.txt                                                       
-a----         2026/7/16     17:30           1881 CONTRIBUTING.md                                                      
-a----         2026/7/16     16:18           4484 improvement_plan.md                                                  
-a----          2026/7/4     14:03           1069 LICENSE                                                              
-a----         2026/7/16     17:02           6144 project_status.md                                                    
-a----         2026/7/16     16:32           3641 prompt_p0_build.md                                                   
-a----         2026/7/16     16:52           5077 prompt_p1_benchmark.md                                               
-a----         2026/7/16     16:48            867 pyproject.toml                                                       
-a----         2026/7/16     17:28          14342 README.md                                                            
-a----         2026/7/16     16:48            405 SECURITY.md                                                          
-a----         2026/7/12     19:58          62758 social-preview.png                                                   
-a----          2026/7/4     13:16           8665 verify_batch.py                                                      
-a----          2026/7/4     14:19           9507 verify_etf_core.py                                                   



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; @'"'
from pathlib import Path
root = Path(r'E:\\workspace\\projects\\形态匹配ETF策略-pybind11')
paths = [
    root/'src/cpp/etf_core.cpp',
    root/'src/cpp/etf_core.hpp',
    root/'CMakeLists.txt',
    root/'tests/CMakeLists.txt',
    root/'tests/test_etf_core.cpp',
    root/'verify_etf_core.py',
    root/'verify_batch.py',
]
for p in paths:
    print(f'--- {p.relative_to(root)} ---')
    if not p.exists():
        print('(missing)')
        continue
    data = p.read_bytes()
    if data.startswith(b'\\xef\\xbb\\xbf'):
        enc = 'utf-8-sig'
    else:
        try:
            data.decode('utf-8')
            enc = 'utf-8'
        except UnicodeDecodeError:
            enc = 'non-utf8 (likely GBK)'
    crlf = data.count(b'\\r\\n')
    lf = data.count(b'\\n')
    print(f'encoding={enc}, bytes={len(data)}, CRLF={crlf}, LF={lf}')
'@ | python -; Write-Host '--- git status ---'; git status --short; Write-Host '--- src/cpp ---'; Get-ChildItem -LiteralPath 'src\\cpp' -Force; Write-Host '--- tests ---'; Get-ChildItem -LiteralPath 'tests' -Force" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 239ms:
--- git status ---
 M project_status.md
?? _review/
?? docs/reviews/performance-analysis-review-kimi.md
?? improvement_plan.md
?? notebooks/01_price_series.png
?? notebooks/02_query_window.png
?? notebooks/03_cosine_prefilter.png
?? notebooks/04_dtw_warping.png
?? notebooks/05_feature_evolution.png
?? notebooks/06_trading_signals.png
?? notebooks/07_batch_dtw.png
?? notebooks/08_benchmark.png
?? prompt_p0_build.md
?? prompt_p1_benchmark.md
--- src/cpp ---


    目录: E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d-----         2026/7/12     19:41                pyi                                                                  
-a----          2026/7/3     23:25            447 CMakeLists.txt                                                       
-a----         2026/7/12     19:41          44567 etf_core.cpp                                                         
-a----         2026/7/16     16:48            428 __init__.py                                                          
--- tests ---


    目录: E:\workspace\projects\形态匹配ETF策略-pybind11\tests


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d-----         2026/7/12     19:41                __pycache__                                                          
-a----         2026/7/12     19:41           8532 test_dtw.py                                                          
-a----          2026/7/3     23:02           9229 test_pattern_match.py                                                
-a----          2026/7/4     13:17           5406 test_technical.py                                                    


  File "<stdin>", line 1
    \ufefffrom pathlib import Path
    ^
SyntaxError: invalid non-printable character U+FEFF

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Host '"'--- encoding/newline metadata ---'; "'$files = @('"'src/cpp/etf_core.cpp','src/cpp/CMakeLists.txt','CMakeLists.txt','verify_etf_core.py','verify_batch.py'); foreach ("'$f in $files) { $p = (Resolve-Path -LiteralPath $f).Path; $bytes = [System.IO.File]::ReadAllBytes($p); $bom = ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF); try { $utf8 = [System.Text.UTF8Encoding]::new($false, $true); [void]$utf8.GetString($bytes); $enc = if ($bom) {'"'UTF-8 BOM'} else {'UTF-8 no BOM'} } catch { "'$enc = '"'not strict UTF-8' }; "'$crlf = 0; $lf = 0; for ($i=0; $i -lt $bytes.Length; $i++) { if ($bytes[$i] -eq 10) { $lf++; if ($i -gt 0 -and $bytes[$i-1] -eq 13) { $crlf++ } } }; Write-Host "$f :: $enc :: CRLF=$crlf LF=$lf bytes=$($bytes.Length)" }; Write-Host '"'--- root CMakeLists.txt ---'; Get-Content -LiteralPath 'CMakeLists.txt' -Raw -Encoding UTF8; Write-Host '--- src/cpp/CMakeLists.txt ---'; Get-Content -LiteralPath 'src/cpp/CMakeLists.txt' -Raw -Encoding UTF8; Write-Host '--- function-like definitions ---'; Select-String -LiteralPath 'src/cpp/etf_core.cpp' -Pattern '"'^([A-Za-z_][A-Za-z0-9_:<> ,&*]+)'"\\s+[A-Za-z_][A-Za-z0-9_]*\\s*\\(' -Encoding UTF8 | ForEach-Object { \"{0}:{1}\" -f "'$_.LineNumber,$_.Line.Trim() }; Write-Host '"'--- PYBIND exports ---'; Select-String -LiteralPath 'src/cpp/etf_core.cpp' -Pattern 'm\\.def|PYBIND11_MODULE' -Encoding UTF8 | ForEach-Object { \"{0}:{1}\" -f "'$_.LineNumber,$_.Line.Trim() }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 284ms:
--- encoding/newline metadata ---
src/cpp/etf_core.cpp :: UTF-8 no BOM :: CRLF=1082 LF=1082 bytes=44567
src/cpp/CMakeLists.txt :: UTF-8 no BOM :: CRLF=0 LF=10 bytes=447
CMakeLists.txt :: UTF-8 no BOM :: CRLF=64 LF=64 bytes=2653
verify_etf_core.py :: UTF-8 no BOM :: CRLF=0 LF=310 bytes=9507
verify_batch.py :: UTF-8 no BOM :: CRLF=0 LF=263 bytes=8665
--- root CMakeLists.txt ---
cmake_minimum_required(VERSION 3.20)

# ──────────────────────────────────────────────
# 形态匹配ETF策略 — C++ 加速模块
# > 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
# > 复用 pybind11-demo 已验证的 MSVC 配置
# > v2: 三模块合并为单 etf_core, /utf-8 优先
# ──────────────────────────────────────────────

project(etf_pattern_match LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Python
set(Python_EXECUTABLE "" CACHE FILEPATH "Path to python.exe")
if(Python_EXECUTABLE)
    get_filename_component(Python_ROOT_DIR "${Python_EXECUTABLE}" DIRECTORY)
endif()
if(NOT Python_EXECUTABLE)
    message(WARNING
        "Python_EXECUTABLE not set. "
        "Use -DPython_EXECUTABLE=/path/to/python.exe to specify which Python to use.\n"
        "  Example: cmake -B build -DPython_EXECUTABLE=<path-to-python.exe>")
endif()
find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Module)

# pybind11 — auto-detect
set(pybind11_DIR "" CACHE PATH "pybind11 cmake config dir")
if(NOT pybind11_DIR)
    execute_process(
        COMMAND "${Python_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE _pybind11_cmake_dir OUTPUT_STRIP_TRAILING_WHITESPACE ERROR_QUIET
    )
    if(_pybind11_cmake_dir)
        set(pybind11_DIR "${_pybind11_cmake_dir}")
    endif()
endif()
if(NOT pybind11_DIR)
    message(FATAL_ERROR
        "pybind11 not found!\n"
        "  Install: pip install pybind11\n"
        "  Verify:  python -c \"import pybind11; print(pybind11.__version__)\"\n"
        "  Or set:  -Dpybind11_DIR=/path/to/share/cmake/pybind11\n"
        "  Or set:  -DPython_EXECUTABLE=/path/to/python.exe (auto-detect uses this Python)")
endif()
find_package(pybind11 REQUIRED CONFIG)

# MSVC — v2: 优先 /utf-8，/wd4819 为后备
if(MSVC)
    add_compile_options("$<$<CONFIG:Release>:/O2>")
    add_compile_options(/utf-8 /wd4819)
endif()

# 子目录 — C++ 模块
add_subdirectory(src/cpp)

# Install — scikit-build-core 需要这些指令来打包 wheel
install(TARGETS etf_core DESTINATION src/cpp)
# Also expose the extension at the top level for ``import etf_core`` after pip install.
install(TARGETS etf_core DESTINATION .)
# Match scikit-build-core's wheel package destination (``cpp``) as well.
install(TARGETS etf_core DESTINATION cpp)

--- src/cpp/CMakeLists.txt ---
# C++ 加速模块 — 统一 etf_core 模块
# v2 修订：三模块合并为一个，减少 ABI 管理复杂度和重复样板代码
# v3: 固定输出到 build/ (MSVC 加 config 子目录 → build/Release/)

pybind11_add_module(etf_core MODULE etf_core.cpp)
set_target_properties(etf_core PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)
message(STATUS "C++ module: etf_core")

--- function-like definitions ---
61:std::vector<double> standardize_returns_cpp(const double* prices, py::ssize_t n) {
104:ArrD standardize_returns(ArrD price_series) {
128:double cosine_similarity(ArrD x_arr, ArrD y_arr) {
165:double dtw_distance_span(const double* x, py::ssize_t n,
201:double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
222:double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
291:ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
367:std::vector<double> extract_window(const double* prices, py::ssize_t start, py::ssize_t end) {
377:double cosine_similarity_vec(const std::vector<double>& x, const std::vector<double>& y) {
399:inline double dtw_distance_vec(const std::vector<double>& x, const std::vector<double>& y, int window = 5) {
405:py::object dtw_distance_batch(
473:PatternResult compute_pattern_features_cpp(
551:std::optional<PatternResult> pattern_match_core(
714:py::object pattern_match_single(
811:py::tuple pattern_match_batch(
--- PYBIND exports ---
8:* >     compute_adx, compute_atr, pattern_match_single, 模块骨架, PYBIND11_MODULE
975:PYBIND11_MODULE(etf_core, m) {
985:m.def("standardize_returns", &standardize_returns,
991:m.def("cosine_similarity", &cosine_similarity,
997:m.def("dtw_distance", &dtw_distance,
1003:m.def("dtw_distance_batch", &dtw_distance_batch,
1016:m.def("compute_adx", &compute_adx,
1022:m.def("compute_atr", &compute_atr,
1048:m.def("pattern_match_single", &pattern_match_single,
1069:m.def("pattern_match_batch", &pattern_match_batch,

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'src/cpp/etf_core.cpp' -Encoding UTF8; for ("'$i=0; $i -lt [Math]::Min(450,$lines.Count); $i++) { '"'{0,4}: {1}' -f ("'$i+1), $lines[$i] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 190ms:
   1: /**
   2:  * etf_core.cpp — 形态匹配ETF策略 C++ 加速模块 (pybind11)
   3:  * =============================================================
   4:  *
   5:  * > 模型 provenance:
   6:  * >   DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03:
   7:  * >     standardize_returns, cosine_similarity, dtw_distance,
   8:  * >     compute_adx, compute_atr, pattern_match_single, 模块骨架, PYBIND11_MODULE
   9:  * >   Kimi-K2.7-Code (via Kimi Code CLI), 2026-07-03:
  10:  * >     pattern_match_batch, cosine_similarity_vec, dtw_distance_vec,
  11:  * >     compute_pattern_features_cpp, 预计算缓存架构, v3 修订
  12:  * >   DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-12:
  13:  * >     dtw_distance_batch, 模块绑定
  14:  *
  15:  * 来源: 形态匹配ETF组合策略_V3.3.py
  16:  *   - dtw_distance:         行 339-359
  17:  *   - standardize_returns:  行 362-373
  18:  *   - cosine_similarity:    行 376-382
  19:  *   - _compute_adx_from_df: 行 757-795
  20:  *   - pattern_match_single: 行 389-627 (含 V3.0 余弦预筛选)
  21:  *   - pattern_match_batch:  新增 — 同 ETF 多 T_idx 批量形态匹配
  22:  *
  23:  * 工具链: MSVC 19.51 + pybind11 3.0.4 + C++20
  24:  * 编译:   cmake -B build -DPython_EXECUTABLE=... && cmake --build build --config Release
  25:  *
  26:  * 审查: Kimi-K2.7-Code (魔鬼代言人) + GPT-5.5 via Codex CLI (完备性)
  27:  *
  28:  * v2 修订 (基于双审):
  29:  *   - 三模块合并为一个 etf_core
  30:  *   - GIL释放边界明确标注
  31:  *   - py::ssize_t 索引 (MSVC兼容)
  32:  *   - forcecast 策略处理 dtype
  33:  *   - 浮点容差分两层 (距离 <1e-8, 得分 <1e-6)
  34:  *   - 返回结构契约: dict key 稳定, None 语义一致
  35:  *
  36:  * v3 修订:
  37:  *   - 新增 pattern_match_batch，消除同 ETF 多 T_idx 场景下的 Python 往返和重复标准化
  38:  */
  39: 
  40: #include <pybind11/pybind11.h>
  41: #include <pybind11/numpy.h>
  42: #include <pybind11/stl.h>
  43: #include <cmath>
  44: #include <vector>
  45: #include <algorithm>
  46: #include <limits>
  47: #include <numeric>
  48: #include <optional>
  49: #include <stdexcept>
  50: 
  51: namespace py = pybind11;
  52: 
  53: // ── 类型别名 (v2: forcecast 策略) ──
  54: using ArrD  = py::array_t<double, py::array::c_style | py::array::forcecast>;
  55: using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;
  56: 
  57: // ═══════════════════════════════════════════════════════════════
  58: // 第一部分: 序列标准化 (V3.3.py 行 362-373)
  59: // ═══════════════════════════════════════════════════════════════
  60: 
  61: std::vector<double> standardize_returns_cpp(const double* prices, py::ssize_t n) {
  62:     if (n < 2) {
  63:         return {};  // 返回空向量表示无效窗口
  64:     }
  65: 
  66:     // 窗口级检查：任一价格为非有限值 → 整个窗口无效
  67:     for (py::ssize_t i = 0; i < n; ++i) {
  68:         if (!std::isfinite(prices[i])) {
  69:             return {};
  70:         }
  71:     }
  72: 
  73:     // 计算对数收益率（所有价格已通过有限性检查，长度固定为 n-1）
  74:     std::vector<double> rets;
  75:     rets.reserve(n - 1);
  76:     for (py::ssize_t i = 1; i < n; ++i) {
  77:         double p_prev = std::max(prices[i - 1], 1e-12);
  78:         double p_curr = std::max(prices[i], 1e-12);
  79:         rets.push_back(std::log(p_curr / p_prev));
  80:     }
  81: 
  82:     if (rets.empty()) {
  83:         return {};
  84:     }
  85: 
  86:     // 去均值
  87:     double mean = std::accumulate(rets.begin(), rets.end(), 0.0) / rets.size();
  88:     for (auto& r : rets) r -= mean;
  89: 
  90:     // 标准差
  91:     double sq_sum = 0.0;
  92:     for (auto r : rets) sq_sum += r * r;
  93:     double std_val = std::sqrt(sq_sum / rets.size());
  94: 
  95:     if (std_val < 1e-12) {
  96:         return rets;  // 已去均值，不再除以 std
  97:     }
  98: 
  99:     for (auto& r : rets) r /= std_val;
 100:     return rets;
 101: }
 102: 
 103: // Python 绑定包装
 104: ArrD standardize_returns(ArrD price_series) {
 105:     auto buf = price_series.unchecked<1>();
 106:     py::ssize_t n = buf.shape(0);
 107:     const double* ptr = buf.data(0);
 108: 
 109:     std::vector<double> result_vec;
 110:     {
 111:         py::gil_scoped_release release;
 112:         result_vec = standardize_returns_cpp(ptr, n);
 113:     }
 114: 
 115:     py::ssize_t m = static_cast<py::ssize_t>(result_vec.size());
 116:     ArrD result(m);
 117:     auto res_buf = result.mutable_unchecked<1>();
 118:     for (py::ssize_t i = 0; i < m; ++i) {
 119:         res_buf(i) = result_vec[i];
 120:     }
 121:     return result;
 122: }
 123: 
 124: // ═══════════════════════════════════════════════════════════════
 125: // 第二部分: 余弦相似度 (V3.3.py 行 376-382)
 126: // ═══════════════════════════════════════════════════════════════
 127: 
 128: double cosine_similarity(ArrD x_arr, ArrD y_arr) {
 129:     auto x = x_arr.unchecked<1>();
 130:     auto y = y_arr.unchecked<1>();
 131:     py::ssize_t n = x.shape(0);
 132: 
 133:     if (n != y.shape(0)) {
 134:         throw std::invalid_argument("x and y must have same length");
 135:     }
 136: 
 137:     const double* xp = x.data(0);
 138:     const double* yp = y.data(0);
 139: 
 140:     double dot, norm_x2, norm_y2;
 141:     {
 142:         py::gil_scoped_release release;
 143:         dot = 0.0; norm_x2 = 0.0; norm_y2 = 0.0;
 144:         for (py::ssize_t i = 0; i < n; ++i) {
 145:             dot += xp[i] * yp[i];
 146:             norm_x2 += xp[i] * xp[i];
 147:             norm_y2 += yp[i] * yp[i];
 148:         }
 149:     }
 150: 
 151:     double norm_x = std::sqrt(norm_x2);
 152:     double norm_y = std::sqrt(norm_y2);
 153:     if (norm_x < 1e-12 || norm_y < 1e-12) {
 154:         return 0.0;
 155:     }
 156:     return dot / (norm_x * norm_y);
 157: }
 158: 
 159: // ═══════════════════════════════════════════════════════════════
 160: // 第三部分: DTW 距离 (V3.3.py 行 339-359)
 161: // ═══════════════════════════════════════════════════════════════
 162: 
 163: // Span版 DTW 距离（零拷贝 + 滚动双行数组，O(m) 内存）
 164: // 供 public API 和内部批量函数共用
 165: double dtw_distance_span(const double* x, py::ssize_t n,
 166:                           const double* y, py::ssize_t m,
 167:                           int window = 5) {
 168:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 169: 
 170:     int band = std::max(window, static_cast<int>(std::abs(n - m)));
 171:     const double INF = std::numeric_limits<double>::infinity();
 172: 
 173:     std::vector<double> prev(m + 1, INF);
 174:     std::vector<double> curr(m + 1, INF);
 175:     prev[0] = 0.0;
 176: 
 177:     for (py::ssize_t i = 1; i <= n; ++i) {
 178:         py::ssize_t j_start = std::max(py::ssize_t(1), i - band);
 179:         py::ssize_t j_end = std::min(m, i + band);
 180: 
 181:         for (py::ssize_t j = j_start; j <= j_end; ++j) {
 182:             double cost = x[i - 1] - y[j - 1];
 183:             cost *= cost;
 184: 
 185:             double pj = (std::abs((i - 1) - j) <= band) ? prev[j] : INF;
 186:             double cj = (j > j_start) ? curr[j - 1] : INF;
 187:             double pj1 = prev[j - 1];
 188: 
 189:             curr[j] = cost + std::min({pj, cj, pj1});
 190:         }
 191: 
 192:         std::swap(prev, curr);
 193:         // dtw[i][0] = INF for all i > 0（prev[0] 经 swap 可能残留 0.0）
 194:         prev[0] = INF;
 195:     }
 196: 
 197:     double path_len = static_cast<double>(n + m);
 198:     return (path_len > 0) ? std::sqrt(prev[m]) / path_len : INF;
 199: }
 200: 
 201: double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
 202:     auto x = x_arr.unchecked<1>();
 203:     auto y = y_arr.unchecked<1>();
 204:     py::ssize_t n = x.shape(0);
 205:     py::ssize_t m = y.shape(0);
 206: 
 207:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 208: 
 209:     double result;
 210:     {
 211:         py::gil_scoped_release release;
 212:         result = dtw_distance_span(x.data(0), n, y.data(0), m, window);
 213:     }
 214: 
 215:     return result;
 216: }
 217: 
 218: // ═══════════════════════════════════════════════════════════════
 219: // 第四部分: ADX 计算 (V3.3.py 行 757-795)
 220: // ═══════════════════════════════════════════════════════════════
 221: 
 222: double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 223:     if (n <= 0) {
 224:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 225:     }
 226:     auto high = high_arr.unchecked<1>();
 227:     auto low  = low_arr.unchecked<1>();
 228:     auto close = close_arr.unchecked<1>();
 229:     py::ssize_t len = high.shape(0);
 230: 
 231:     if (len < n + 16) return 25.0;
 232:     if (low.shape(0) != len || close.shape(0) != len) {
 233:         throw std::invalid_argument("high/low/close must have same length");
 234:     }
 235: 
 236:     double result;
 237:     {
 238:         py::gil_scoped_release release;
 239: 
 240:         py::ssize_t tr_len = len - 1;
 241:         std::vector<double> tr(tr_len), plus_dm(tr_len), minus_dm(tr_len);
 242: 
 243:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 244:             double hl = high(i + 1) - low(i + 1);
 245:             double hc = std::abs(high(i + 1) - close(i));
 246:             double lc = std::abs(low(i + 1) - close(i));
 247:             tr[i] = std::max({hl, hc, lc});
 248: 
 249:             double up = high(i + 1) - high(i);
 250:             double down = low(i) - low(i + 1);
 251:             plus_dm[i]  = (up > down && up > 0) ? up : 0.0;
 252:             minus_dm[i] = (down > up && down > 0) ? down : 0.0;
 253:         }
 254: 
 255:         // Wilder's smoothing
 256:         auto wilder_smooth = [&](const std::vector<double>& raw) {
 257:             std::vector<double> smoothed(tr_len, 0.0);
 258:             double init_sum = 0.0;
 259:             for (int i = 0; i < n; ++i) init_sum += raw[i];
 260:             // Fill first n positions with initial mean (match Python behaviour)
 261:             double init_mean = init_sum / n;
 262:             for (int i = 0; i < n; ++i) smoothed[i] = init_mean;
 263:             for (py::ssize_t i = n; i < tr_len; ++i) {
 264:                 smoothed[i] = (smoothed[i - 1] * (n - 1) + raw[i]) / n;
 265:             }
 266:             return smoothed;
 267:         };
 268: 
 269:         auto atr_s = wilder_smooth(tr);
 270:         auto plus_s = wilder_smooth(plus_dm);
 271:         auto minus_s = wilder_smooth(minus_dm);
 272: 
 273:         std::vector<double> dx(tr_len);
 274:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 275:             double pdi = 100.0 * plus_s[i] / (atr_s[i] + 1e-12);
 276:             double mdi = 100.0 * minus_s[i] / (atr_s[i] + 1e-12);
 277:             dx[i] = 100.0 * std::abs(pdi - mdi) / (pdi + mdi + 1e-12);
 278:         }
 279: 
 280:         auto adx_s = wilder_smooth(dx);
 281:         result = adx_s.back();
 282:     }
 283: 
 284:     return result;
 285: }
 286: 
 287: // ═══════════════════════════════════════════════════════════════
 288: // 第五部分: ATR 计算
 289: // ═══════════════════════════════════════════════════════════════
 290: 
 291: ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 292:     if (n <= 0) {
 293:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 294:     }
 295:     auto high = high_arr.unchecked<1>();
 296:     auto low  = low_arr.unchecked<1>();
 297:     auto close = close_arr.unchecked<1>();
 298:     py::ssize_t len = high.shape(0);
 299: 
 300:     // v3: 输入校验 (GPT-5.5 最终审查 P0)
 301:     if (low.shape(0) != len || close.shape(0) != len) {
 302:         throw std::invalid_argument("high/low/close must have same length");
 303:     }
 304:     if (len < n + 1) {
 305:         ArrD result(len);
 306:         auto res = result.mutable_unchecked<1>();
 307:         for (py::ssize_t i = 0; i < len; ++i)
 308:             res(i) = std::numeric_limits<double>::quiet_NaN();
 309:         return result;
 310:     }
 311: 
 312:     const double* hp = high.data(0);
 313:     const double* lp = low.data(0);
 314:     const double* cp = close.data(0);
 315: 
 316:     ArrD result(len);
 317:     auto res = result.mutable_unchecked<1>();
 318:     for (py::ssize_t i = 0; i < n; ++i) res(i) = std::numeric_limits<double>::quiet_NaN();
 319: 
 320:     {
 321:         py::gil_scoped_release release;
 322: 
 323:         py::ssize_t tr_len = len - 1;
 324:         std::vector<double> tr(tr_len);
 325: 
 326:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 327:             double hl = hp[i + 1] - lp[i + 1];
 328:             double hc = std::abs(hp[i + 1] - cp[i]);
 329:             double lc = std::abs(lp[i + 1] - cp[i]);
 330:             tr[i] = std::max({hl, hc, lc});
 331:         }
 332: 
 333:         double init_sum = 0.0;
 334:         for (int i = 0; i < n; ++i) init_sum += tr[i];
 335:         res(n) = init_sum / n;
 336: 
 337:         for (py::ssize_t i = n + 1; i < len; ++i) {
 338:             res(i) = (res(i - 1) * (n - 1) + tr[i - 1]) / n;
 339:         }
 340:     }
 341:     return result;
 342: }
 343: 
 344: // ═══════════════════════════════════════════════════════════════
 345: // 第六部分: 形态匹配引擎 (V3.3.py 行 389-627)
 346: // ═══════════════════════════════════════════════════════════════
 347: 
 348: namespace {
 349: 
 350: struct MatchCandidate {
 351:     py::ssize_t hist_end;
 352:     py::ssize_t hist_start;
 353:     double cos_s;
 354:     std::vector<double> hist_rets;
 355: };
 356: 
 357: struct PatternResult {
 358:     double top1_sim, top5_avg_sim, sim_decay, sim_variance;
 359:     double match_distance_ratio, avg_future_ret, weighted_future_ret;
 360:     double median_future_ret, ret_sign_consistency, best_match_ret;
 361:     double max_dd_in_matches, match_time_span, match_time_span_ratio;
 362:     double match_cluster_ratio;
 363:     int n_matches_above_thresh;
 364: };
 365: 
 366: // 从价格数组提取窗口
 367: std::vector<double> extract_window(const double* prices, py::ssize_t start, py::ssize_t end) {
 368:     std::vector<double> result;
 369:     result.reserve(end - start + 1);
 370:     for (py::ssize_t i = start; i <= end; ++i) {
 371:         result.push_back(prices[i]);
 372:     }
 373:     return result;
 374: }
 375: 
 376: // 向量版余弦相似度（用于批量内部计算）
 377: double cosine_similarity_vec(const std::vector<double>& x, const std::vector<double>& y) {
 378:     py::ssize_t n = static_cast<py::ssize_t>(x.size());
 379:     if (n != static_cast<py::ssize_t>(y.size())) {
 380:         return 0.0;
 381:     }
 382:     if (n == 0) return 0.0;
 383: 
 384:     double dot = 0.0, norm_x2 = 0.0, norm_y2 = 0.0;
 385:     for (py::ssize_t i = 0; i < n; ++i) {
 386:         dot += x[i] * y[i];
 387:         norm_x2 += x[i] * x[i];
 388:         norm_y2 += y[i] * y[i];
 389:     }
 390:     double norm_x = std::sqrt(norm_x2);
 391:     double norm_y = std::sqrt(norm_y2);
 392:     if (norm_x < 1e-12 || norm_y < 1e-12) {
 393:         return 0.0;
 394:     }
 395:     return dot / (norm_x * norm_y);
 396: }
 397: 
 398: // 向量版 DTW（兼容旧调用，委托给 span 版）
 399: inline double dtw_distance_vec(const std::vector<double>& x, const std::vector<double>& y, int window = 5) {
 400:     return dtw_distance_span(x.data(), static_cast<py::ssize_t>(x.size()),
 401:                               y.data(), static_cast<py::ssize_t>(y.size()), window);
 402: }
 403: 
 404: // 批量 DTW: 一个 query 对 N 个 candidates（一对一远端循环，GIL 释放）
 405: py::object dtw_distance_batch(
 406:     ArrD query_arr,
 407:     ArrD candidates_arr,
 408:     int window = 5,
 409:     int top_k = 0
 410: ) {
 411:     auto q = query_arr.unchecked<1>();
 412:     auto c = candidates_arr.unchecked<2>();
 413:     py::ssize_t L = q.shape(0);
 414:     py::ssize_t N = c.shape(0);
 415: 
 416:     if (N == 0) {
 417:         if (top_k > 0) {
 418:             ArrI64 empty_idx(0);
 419:             ArrD empty_dist(0);
 420:             return py::make_tuple(empty_idx, empty_dist);
 421:         }
 422:         ArrD empty_result(0);
 423:         return empty_result;
 424:     }
 425: 
 426:     if (c.shape(1) != L) {
 427:         throw std::invalid_argument(
 428:             "candidates.shape[1] must equal query length, got " +
 429:             std::to_string(c.shape(1)) + " vs " + std::to_string(L));
 430:     }
 431: 
 432:     std::vector<double> distances(N);
 433: 
 434:     {
 435:         py::gil_scoped_release release;
 436:         const double* q_ptr = q.data(0);
 437:         for (py::ssize_t i = 0; i < N; ++i) {
 438:             distances[i] = dtw_distance_span(q_ptr, L, c.data(i, 0), L, window);
 439:         }
 440:     }
 441: 
 442:     if (top_k <= 0 || top_k >= static_cast<int>(N)) {
 443:         ArrD result(N);
 444:         auto res_buf = result.mutable_unchecked<1>();
 445:         for (py::ssize_t i = 0; i < N; ++i) res_buf(i) = distances[i];
 446:         return result;
 447:     }
 448: 
 449:     // Top-K via partial_sort
 450:     std::vector<std::pair<double, py::ssize_t>> indexed;

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'src/cpp/etf_core.cpp' -Encoding UTF8; foreach ("'$range in @(@(100,230),@(231,343))) { Write-Host "--- lines $($range[0])-$($range[1]) ---"; for ($i=$range[0]-1; $i -lt [Math]::Min($range[1],$lines.Count); $i++) { '"'{0,4}: {1}' -f ("'$i+1), $lines[$i] } }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 218ms:
--- lines 100-230 ---
 100:     return rets;
 101: }
 102: 
 103: // Python 绑定包装
 104: ArrD standardize_returns(ArrD price_series) {
 105:     auto buf = price_series.unchecked<1>();
 106:     py::ssize_t n = buf.shape(0);
 107:     const double* ptr = buf.data(0);
 108: 
 109:     std::vector<double> result_vec;
 110:     {
 111:         py::gil_scoped_release release;
 112:         result_vec = standardize_returns_cpp(ptr, n);
 113:     }
 114: 
 115:     py::ssize_t m = static_cast<py::ssize_t>(result_vec.size());
 116:     ArrD result(m);
 117:     auto res_buf = result.mutable_unchecked<1>();
 118:     for (py::ssize_t i = 0; i < m; ++i) {
 119:         res_buf(i) = result_vec[i];
 120:     }
 121:     return result;
 122: }
 123: 
 124: // ═══════════════════════════════════════════════════════════════
 125: // 第二部分: 余弦相似度 (V3.3.py 行 376-382)
 126: // ═══════════════════════════════════════════════════════════════
 127: 
 128: double cosine_similarity(ArrD x_arr, ArrD y_arr) {
 129:     auto x = x_arr.unchecked<1>();
 130:     auto y = y_arr.unchecked<1>();
 131:     py::ssize_t n = x.shape(0);
 132: 
 133:     if (n != y.shape(0)) {
 134:         throw std::invalid_argument("x and y must have same length");
 135:     }
 136: 
 137:     const double* xp = x.data(0);
 138:     const double* yp = y.data(0);
 139: 
 140:     double dot, norm_x2, norm_y2;
 141:     {
 142:         py::gil_scoped_release release;
 143:         dot = 0.0; norm_x2 = 0.0; norm_y2 = 0.0;
 144:         for (py::ssize_t i = 0; i < n; ++i) {
 145:             dot += xp[i] * yp[i];
 146:             norm_x2 += xp[i] * xp[i];
 147:             norm_y2 += yp[i] * yp[i];
 148:         }
 149:     }
 150: 
 151:     double norm_x = std::sqrt(norm_x2);
 152:     double norm_y = std::sqrt(norm_y2);
 153:     if (norm_x < 1e-12 || norm_y < 1e-12) {
 154:         return 0.0;
 155:     }
 156:     return dot / (norm_x * norm_y);
 157: }
 158: 
 159: // ═══════════════════════════════════════════════════════════════
 160: // 第三部分: DTW 距离 (V3.3.py 行 339-359)
 161: // ═══════════════════════════════════════════════════════════════
 162: 
 163: // Span版 DTW 距离（零拷贝 + 滚动双行数组，O(m) 内存）
 164: // 供 public API 和内部批量函数共用
 165: double dtw_distance_span(const double* x, py::ssize_t n,
 166:                           const double* y, py::ssize_t m,
 167:                           int window = 5) {
 168:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 169: 
 170:     int band = std::max(window, static_cast<int>(std::abs(n - m)));
 171:     const double INF = std::numeric_limits<double>::infinity();
 172: 
 173:     std::vector<double> prev(m + 1, INF);
 174:     std::vector<double> curr(m + 1, INF);
 175:     prev[0] = 0.0;
 176: 
 177:     for (py::ssize_t i = 1; i <= n; ++i) {
 178:         py::ssize_t j_start = std::max(py::ssize_t(1), i - band);
 179:         py::ssize_t j_end = std::min(m, i + band);
 180: 
 181:         for (py::ssize_t j = j_start; j <= j_end; ++j) {
 182:             double cost = x[i - 1] - y[j - 1];
 183:             cost *= cost;
 184: 
 185:             double pj = (std::abs((i - 1) - j) <= band) ? prev[j] : INF;
 186:             double cj = (j > j_start) ? curr[j - 1] : INF;
 187:             double pj1 = prev[j - 1];
 188: 
 189:             curr[j] = cost + std::min({pj, cj, pj1});
 190:         }
 191: 
 192:         std::swap(prev, curr);
 193:         // dtw[i][0] = INF for all i > 0（prev[0] 经 swap 可能残留 0.0）
 194:         prev[0] = INF;
 195:     }
 196: 
 197:     double path_len = static_cast<double>(n + m);
 198:     return (path_len > 0) ? std::sqrt(prev[m]) / path_len : INF;
 199: }
 200: 
 201: double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
 202:     auto x = x_arr.unchecked<1>();
 203:     auto y = y_arr.unchecked<1>();
 204:     py::ssize_t n = x.shape(0);
 205:     py::ssize_t m = y.shape(0);
 206: 
 207:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 208: 
 209:     double result;
 210:     {
 211:         py::gil_scoped_release release;
 212:         result = dtw_distance_span(x.data(0), n, y.data(0), m, window);
 213:     }
 214: 
 215:     return result;
 216: }
 217: 
 218: // ═══════════════════════════════════════════════════════════════
 219: // 第四部分: ADX 计算 (V3.3.py 行 757-795)
 220: // ═══════════════════════════════════════════════════════════════
 221: 
 222: double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 223:     if (n <= 0) {
 224:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 225:     }
 226:     auto high = high_arr.unchecked<1>();
 227:     auto low  = low_arr.unchecked<1>();
 228:     auto close = close_arr.unchecked<1>();
 229:     py::ssize_t len = high.shape(0);
 230: 
--- lines 231-343 ---
 231:     if (len < n + 16) return 25.0;
 232:     if (low.shape(0) != len || close.shape(0) != len) {
 233:         throw std::invalid_argument("high/low/close must have same length");
 234:     }
 235: 
 236:     double result;
 237:     {
 238:         py::gil_scoped_release release;
 239: 
 240:         py::ssize_t tr_len = len - 1;
 241:         std::vector<double> tr(tr_len), plus_dm(tr_len), minus_dm(tr_len);
 242: 
 243:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 244:             double hl = high(i + 1) - low(i + 1);
 245:             double hc = std::abs(high(i + 1) - close(i));
 246:             double lc = std::abs(low(i + 1) - close(i));
 247:             tr[i] = std::max({hl, hc, lc});
 248: 
 249:             double up = high(i + 1) - high(i);
 250:             double down = low(i) - low(i + 1);
 251:             plus_dm[i]  = (up > down && up > 0) ? up : 0.0;
 252:             minus_dm[i] = (down > up && down > 0) ? down : 0.0;
 253:         }
 254: 
 255:         // Wilder's smoothing
 256:         auto wilder_smooth = [&](const std::vector<double>& raw) {
 257:             std::vector<double> smoothed(tr_len, 0.0);
 258:             double init_sum = 0.0;
 259:             for (int i = 0; i < n; ++i) init_sum += raw[i];
 260:             // Fill first n positions with initial mean (match Python behaviour)
 261:             double init_mean = init_sum / n;
 262:             for (int i = 0; i < n; ++i) smoothed[i] = init_mean;
 263:             for (py::ssize_t i = n; i < tr_len; ++i) {
 264:                 smoothed[i] = (smoothed[i - 1] * (n - 1) + raw[i]) / n;
 265:             }
 266:             return smoothed;
 267:         };
 268: 
 269:         auto atr_s = wilder_smooth(tr);
 270:         auto plus_s = wilder_smooth(plus_dm);
 271:         auto minus_s = wilder_smooth(minus_dm);
 272: 
 273:         std::vector<double> dx(tr_len);
 274:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 275:             double pdi = 100.0 * plus_s[i] / (atr_s[i] + 1e-12);
 276:             double mdi = 100.0 * minus_s[i] / (atr_s[i] + 1e-12);
 277:             dx[i] = 100.0 * std::abs(pdi - mdi) / (pdi + mdi + 1e-12);
 278:         }
 279: 
 280:         auto adx_s = wilder_smooth(dx);
 281:         result = adx_s.back();
 282:     }
 283: 
 284:     return result;
 285: }
 286: 
 287: // ═══════════════════════════════════════════════════════════════
 288: // 第五部分: ATR 计算
 289: // ═══════════════════════════════════════════════════════════════
 290: 
 291: ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 292:     if (n <= 0) {
 293:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 294:     }
 295:     auto high = high_arr.unchecked<1>();
 296:     auto low  = low_arr.unchecked<1>();
 297:     auto close = close_arr.unchecked<1>();
 298:     py::ssize_t len = high.shape(0);
 299: 
 300:     // v3: 输入校验 (GPT-5.5 最终审查 P0)
 301:     if (low.shape(0) != len || close.shape(0) != len) {
 302:         throw std::invalid_argument("high/low/close must have same length");
 303:     }
 304:     if (len < n + 1) {
 305:         ArrD result(len);
 306:         auto res = result.mutable_unchecked<1>();
 307:         for (py::ssize_t i = 0; i < len; ++i)
 308:             res(i) = std::numeric_limits<double>::quiet_NaN();
 309:         return result;
 310:     }
 311: 
 312:     const double* hp = high.data(0);
 313:     const double* lp = low.data(0);
 314:     const double* cp = close.data(0);
 315: 
 316:     ArrD result(len);
 317:     auto res = result.mutable_unchecked<1>();
 318:     for (py::ssize_t i = 0; i < n; ++i) res(i) = std::numeric_limits<double>::quiet_NaN();
 319: 
 320:     {
 321:         py::gil_scoped_release release;
 322: 
 323:         py::ssize_t tr_len = len - 1;
 324:         std::vector<double> tr(tr_len);
 325: 
 326:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 327:             double hl = hp[i + 1] - lp[i + 1];
 328:             double hc = std::abs(hp[i + 1] - cp[i]);
 329:             double lc = std::abs(lp[i + 1] - cp[i]);
 330:             tr[i] = std::max({hl, hc, lc});
 331:         }
 332: 
 333:         double init_sum = 0.0;
 334:         for (int i = 0; i < n; ++i) init_sum += tr[i];
 335:         res(n) = init_sum / n;
 336: 
 337:         for (py::ssize_t i = n + 1; i < len; ++i) {
 338:             res(i) = (res(i - 1) * (n - 1) + tr[i - 1]) / n;
 339:         }
 340:     }
 341:     return result;
 342: }
 343: 

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'src/cpp/etf_core.cpp' -Encoding UTF8; for ("'$i=217; $i -lt 236; $i++) { '"'{0,4}: {1}' -f ("'$i+1), $lines[$i] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 142ms:
 218: // ═══════════════════════════════════════════════════════════════
 219: // 第四部分: ADX 计算 (V3.3.py 行 757-795)
 220: // ═══════════════════════════════════════════════════════════════
 221: 
 222: double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 223:     if (n <= 0) {
 224:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 225:     }
 226:     auto high = high_arr.unchecked<1>();
 227:     auto low  = low_arr.unchecked<1>();
 228:     auto close = close_arr.unchecked<1>();
 229:     py::ssize_t len = high.shape(0);
 230: 
 231:     if (len < n + 16) return 25.0;
 232:     if (low.shape(0) != len || close.shape(0) != len) {
 233:         throw std::invalid_argument("high/low/close must have same length");
 234:     }
 235: 
 236:     double result;

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'src/cpp/etf_core.cpp' -Encoding UTF8; foreach ("'$range in @(@(404,550),@(551,713),@(714,850))) { Write-Host "--- lines $($range[0])-$($range[1]) ---"; for ($i=$range[0]-1; $i -lt [Math]::Min($range[1],$lines.Count); $i++) { '"'{0,4}: {1}' -f ("'$i+1), $lines[$i] } }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 217ms:
--- lines 404-550 ---
 404: // 批量 DTW: 一个 query 对 N 个 candidates（一对一远端循环，GIL 释放）
 405: py::object dtw_distance_batch(
 406:     ArrD query_arr,
 407:     ArrD candidates_arr,
 408:     int window = 5,
 409:     int top_k = 0
 410: ) {
 411:     auto q = query_arr.unchecked<1>();
 412:     auto c = candidates_arr.unchecked<2>();
 413:     py::ssize_t L = q.shape(0);
 414:     py::ssize_t N = c.shape(0);
 415: 
 416:     if (N == 0) {
 417:         if (top_k > 0) {
 418:             ArrI64 empty_idx(0);
 419:             ArrD empty_dist(0);
 420:             return py::make_tuple(empty_idx, empty_dist);
 421:         }
 422:         ArrD empty_result(0);
 423:         return empty_result;
 424:     }
 425: 
 426:     if (c.shape(1) != L) {
 427:         throw std::invalid_argument(
 428:             "candidates.shape[1] must equal query length, got " +
 429:             std::to_string(c.shape(1)) + " vs " + std::to_string(L));
 430:     }
 431: 
 432:     std::vector<double> distances(N);
 433: 
 434:     {
 435:         py::gil_scoped_release release;
 436:         const double* q_ptr = q.data(0);
 437:         for (py::ssize_t i = 0; i < N; ++i) {
 438:             distances[i] = dtw_distance_span(q_ptr, L, c.data(i, 0), L, window);
 439:         }
 440:     }
 441: 
 442:     if (top_k <= 0 || top_k >= static_cast<int>(N)) {
 443:         ArrD result(N);
 444:         auto res_buf = result.mutable_unchecked<1>();
 445:         for (py::ssize_t i = 0; i < N; ++i) res_buf(i) = distances[i];
 446:         return result;
 447:     }
 448: 
 449:     // Top-K via partial_sort
 450:     std::vector<std::pair<double, py::ssize_t>> indexed;
 451:     indexed.reserve(N);
 452:     for (py::ssize_t i = 0; i < N; ++i) {
 453:         indexed.emplace_back(distances[i], i);
 454:     }
 455:     std::partial_sort(
 456:         indexed.begin(),
 457:         indexed.begin() + top_k,
 458:         indexed.end());
 459: 
 460:     ArrI64 top_indices(top_k);
 461:     ArrD top_dists(top_k);
 462:     auto idx_buf = top_indices.mutable_unchecked<1>();
 463:     auto dist_buf = top_dists.mutable_unchecked<1>();
 464:     for (int i = 0; i < top_k; ++i) {
 465:         idx_buf(i) = static_cast<int64_t>(indexed[i].second);
 466:         dist_buf(i) = indexed[i].first;
 467:     }
 468: 
 469:     return py::make_tuple(top_indices, top_dists);
 470: }
 471: 
 472: // 从 Top-K 有效匹配中提取 15 维特征
 473: PatternResult compute_pattern_features_cpp(
 474:     const std::vector<double>& valid_scores,
 475:     const std::vector<double>& valid_frets,
 476:     const std::vector<py::ssize_t>& valid_ends,
 477:     int T_back
 478: ) {
 479:     PatternResult r{};
 480:     int top_k_actual = static_cast<int>(valid_scores.size());
 481: 
 482:     // F1-F5: 相似度特征
 483:     r.top1_sim = valid_scores[0];
 484:     int n_avg = std::min(5, top_k_actual);
 485:     double sum_avg = 0.0;
 486:     for (int i = 0; i < n_avg; ++i) sum_avg += valid_scores[i];
 487:     r.top5_avg_sim = sum_avg / n_avg;
 488:     r.sim_decay = r.top1_sim - r.top5_avg_sim;
 489: 
 490:     double var = 0.0, mean_s = 0.0;
 491:     for (auto s : valid_scores) mean_s += s;
 492:     mean_s /= top_k_actual;
 493:     for (auto s : valid_scores) var += (s - mean_s) * (s - mean_s);
 494:     r.sim_variance = (top_k_actual > 1) ? var / top_k_actual : 0.0;
 495:     r.match_distance_ratio = (r.top1_sim > 1e-12) ? r.sim_decay / r.top1_sim : 0.0;
 496: 
 497:     // F6-F11: 后续表现
 498:     double sum_fr = 0.0;
 499:     for (auto fr : valid_frets) sum_fr += fr;
 500:     r.avg_future_ret = sum_fr / top_k_actual;
 501: 
 502:     double sum_ws = 0.0, sum_w = 0.0;
 503:     for (int i = 0; i < top_k_actual; ++i) {
 504:         sum_ws += valid_scores[i] * valid_frets[i];
 505:         sum_w += valid_scores[i];
 506:     }
 507:     r.weighted_future_ret = (sum_w > 1e-12) ? sum_ws / sum_w : r.avg_future_ret;
 508: 
 509:     std::vector<double> sorted_fr = valid_frets;
 510:     std::sort(sorted_fr.begin(), sorted_fr.end());
 511:     r.median_future_ret = (top_k_actual % 2 == 1)
 512:         ? sorted_fr[top_k_actual / 2]
 513:         : (sorted_fr[top_k_actual / 2 - 1] + sorted_fr[top_k_actual / 2]) / 2.0;
 514: 
 515:     int pos_count = 0;
 516:     for (auto fr : valid_frets) if (fr > 0) ++pos_count;
 517:     r.ret_sign_consistency = static_cast<double>(pos_count) / top_k_actual;
 518:     r.best_match_ret = valid_frets[0];
 519: 
 520:     double min_fr = *std::min_element(valid_frets.begin(), valid_frets.end());
 521:     r.max_dd_in_matches = std::max(0.0, -min_fr);
 522: 
 523:     // F12-F15: 匹配质量
 524:     auto [min_e, max_e] = std::minmax_element(valid_ends.begin(), valid_ends.end());
 525:     r.match_time_span = static_cast<double>(*max_e - *min_e);
 526:     r.match_time_span_ratio = r.match_time_span / T_back;
 527: 
 528:     std::vector<py::ssize_t> sorted_ends = valid_ends;
 529:     std::sort(sorted_ends.begin(), sorted_ends.end());
 530:     int max_in_window = 0;
 531:     for (int i = 0; i < top_k_actual; ++i) {
 532:         double target = static_cast<double>(sorted_ends[i]) + 60.0;
 533:         auto it = std::upper_bound(sorted_ends.begin(), sorted_ends.end(),
 534:                                    static_cast<py::ssize_t>(target));
 535:         int count = static_cast<int>(it - sorted_ends.begin()) - i;
 536:         max_in_window = std::max(max_in_window, count);
 537:     }
 538:     r.match_cluster_ratio = static_cast<double>(max_in_window) / top_k_actual;
 539: 
 540:     int above = 0;
 541:     for (auto s : valid_scores) if (s > 0.8) ++above;
 542:     r.n_matches_above_thresh = above;
 543: 
 544:     return r;
 545: }
 546: 
 547: // ═══════════════════════════════════════════════════════════════
 548: // 共享核心：余弦预筛选 → DTW 精排 → 特征提取
 549: // single 和 batch 共用此函数，消除 ~400 行重复逻辑
 550: // ═══════════════════════════════════════════════════════════════
--- lines 551-713 ---
 551: std::optional<PatternResult> pattern_match_core(
 552:     const double* prices, py::ssize_t n_prices,
 553:     int T_idx, int k, int L_query, int T_back,
 554:     int match_step, int M_forward, int dtw_window,
 555:     int cos_prefilter_top,
 556:     const std::vector<double>& query_rets,
 557:     py::ssize_t search_start, py::ssize_t search_end,
 558:     const std::vector<std::vector<double>>* precomputed_rets
 559: ) {
 560:     py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());
 561: 
 562:     // ═══ 第1遍：余弦相似度 + 快速形状距离（全量候选）═══
 563:     std::vector<MatchCandidate> cos_candidates;
 564:     std::vector<double> fast_shape_dists;
 565: 
 566:     for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
 567:         py::ssize_t hist_start = hist_end - L_query + 1;
 568:         if (hist_start < 0) continue;
 569: 
 570:         // 获取标准化收益率：缓存优先，否则现场计算
 571:         const std::vector<double>* hist_rets_ptr = nullptr;
 572:         std::vector<double> hist_rets_scratch;
 573: 
 574:         if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size())) {
 575:             hist_rets_ptr = &(*precomputed_rets)[hist_end];
 576:         } else {
 577:             auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
 578:             if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
 579:                 hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query);
 580:                 hist_rets_ptr = &hist_rets_scratch;
 581:             }
 582:         }
 583: 
 584:         if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;
 585: 
 586:         const auto& hist_rets = *hist_rets_ptr;
 587: 
 588:         // 余弦相似度
 589:         double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
 590:         py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
 591:         for (py::ssize_t i = 0; i < min_len; ++i) {
 592:             dot += hist_rets[i] * query_rets[i];
 593:             nx2 += hist_rets[i] * hist_rets[i];
 594:             ny2 += query_rets[i] * query_rets[i];
 595:         }
 596:         double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
 597:         double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;
 598: 
 599:         // 快速形状距离
 600:         double fast_d2 = 0.0;
 601:         for (py::ssize_t i = 0; i < min_len; ++i) {
 602:             double diff = hist_rets[i] - query_rets[i];
 603:             fast_d2 += diff * diff;
 604:         }
 605:         fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));
 606: 
 607:         if (cos_s > 0) {
 608:             cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
 609:         }
 610:     }
 611: 
 612:     if (cos_candidates.size() < 3) return std::nullopt;
 613: 
 614:     // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
 615:     double sigma_fast = 1.0;
 616:     if (fast_shape_dists.size() > 1) {
 617:         double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0.0)
 618:                         / fast_shape_dists.size();
 619:         double var_fd = 0.0;
 620:         for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
 621:         var_fd /= fast_shape_dists.size();
 622:         sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)));
 623:     }
 624:     sigma_fast = std::max(sigma_fast, 1e-12);
 625: 
 626:     // 余弦排序 + 全量边界
 627:     std::sort(cos_candidates.begin(), cos_candidates.end(),
 628:               [](const MatchCandidate& a, const MatchCandidate& b) { return a.cos_s > b.cos_s; });
 629: 
 630:     double global_min_cos = cos_candidates.back().cos_s;
 631:     double global_max_cos = cos_candidates.front().cos_s;
 632: 
 633:     int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
 634:     cos_candidates.resize(n_cos);
 635: 
 636:     // ═══ 第2遍：DTW 精排 (仅 top-N) ═══
 637:     std::vector<double> dtw_dists, cos_sims, future_rets;
 638:     std::vector<py::ssize_t> match_ends;
 639:     dtw_dists.reserve(n_cos);
 640:     cos_sims.reserve(n_cos);
 641:     future_rets.reserve(n_cos);
 642:     match_ends.reserve(n_cos);
 643: 
 644:     for (const auto& cand : cos_candidates) {
 645:         py::ssize_t hn = static_cast<py::ssize_t>(cand.hist_rets.size());
 646:         double dtw_d = dtw_distance_span(cand.hist_rets.data(), hn,
 647:                                           query_rets.data(), n_query, dtw_window);
 648: 
 649:         dtw_dists.push_back(dtw_d);
 650:         cos_sims.push_back(cand.cos_s);
 651: 
 652:         py::ssize_t fut_end = cand.hist_end + M_forward;
 653:         if (fut_end < n_prices && fut_end < T_idx) {
 654:             future_rets.push_back(prices[fut_end] / prices[cand.hist_end] - 1.0);
 655:         } else {
 656:             future_rets.push_back(std::numeric_limits<double>::quiet_NaN());
 657:         }
 658:         match_ends.push_back(cand.hist_end);
 659:     }
 660: 
 661:     if (dtw_dists.size() < 3) return std::nullopt;
 662: 
 663:     // sim_dtw = exp(-dtw/sigma)
 664:     double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;
 665: 
 666:     std::vector<double> sim_dtw(dtw_dists.size());
 667:     double min_dtw_v = std::numeric_limits<double>::max();
 668:     double max_dtw_v = std::numeric_limits<double>::lowest();
 669:     for (size_t i = 0; i < dtw_dists.size(); ++i) {
 670:         sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
 671:         min_dtw_v = std::min(min_dtw_v, sim_dtw[i]);
 672:         max_dtw_v = std::max(max_dtw_v, sim_dtw[i]);
 673:     }
 674: 
 675:     // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
 676:     double range_dtw = (max_dtw_v - min_dtw_v > 1e-12) ? (max_dtw_v - min_dtw_v) : 1.0;
 677:     double range_cos_val = (global_max_cos - global_min_cos > 1e-12)
 678:                            ? (global_max_cos - global_min_cos) : 1.0;
 679: 
 680:     struct Scored { double score, fut_ret; py::ssize_t end_idx; };
 681:     std::vector<Scored> scored;
 682:     scored.reserve(sim_dtw.size());
 683:     for (size_t i = 0; i < sim_dtw.size(); ++i) {
 684:         double nd = (sim_dtw[i] - min_dtw_v) / range_dtw;
 685:         double nc = (cos_sims[i] - global_min_cos) / range_cos_val;
 686:         scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
 687:     }
 688: 
 689:     std::sort(scored.begin(), scored.end(),
 690:               [](const Scored& a, const Scored& b) { return a.score > b.score; });
 691: 
 692:     int top_k = std::min(k, static_cast<int>(scored.size()));
 693: 
 694:     // 过滤 NaN 未来收益
 695:     std::vector<double> valid_scores, valid_frets;
 696:     std::vector<py::ssize_t> valid_ends;
 697:     for (int i = 0; i < top_k; ++i) {
 698:         if (!std::isnan(scored[i].fut_ret)) {
 699:             valid_scores.push_back(scored[i].score);
 700:             valid_frets.push_back(scored[i].fut_ret);
 701:             valid_ends.push_back(scored[i].end_idx);
 702:         }
 703:     }
 704:     if (valid_scores.size() < 2) return std::nullopt;
 705: 
 706:     return compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);
 707: }
 708: 
 709: } // namespace
 710: 
 711: // ═══════════════════════════════════════════════════════════════
 712: // 第六部分-A: 单点形态匹配（薄包装 → pattern_match_core）
 713: // ═══════════════════════════════════════════════════════════════
--- lines 714-850 ---
 714: py::object pattern_match_single(
 715:     ArrD prices_arr,
 716:     int T_idx,
 717:     int k = 10,
 718:     int L_query = 20,
 719:     int T_back = 750,
 720:     int match_step = 1,
 721:     int M_forward = 5,
 722:     int dtw_window = 5,
 723:     int cos_prefilter_top = 50
 724: ) {
 725:     auto prices_buf = prices_arr.unchecked<1>();
 726:     py::ssize_t n_prices = prices_buf.shape(0);
 727:     const double* prices = prices_buf.data(0);
 728: 
 729:     // ── 输入校验 ──
 730:     if (T_idx < 0 || static_cast<py::ssize_t>(T_idx) >= n_prices) {
 731:         throw std::out_of_range("T_idx must satisfy 0 <= T_idx < len(prices), got " + std::to_string(T_idx));
 732:     }
 733:     if (L_query < 3) {
 734:         throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
 735:     }
 736:     if (T_back <= 0) {
 737:         throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
 738:     }
 739:     if (k <= 0) {
 740:         throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
 741:     }
 742:     if (M_forward < 1) {
 743:         throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
 744:     }
 745:     if (match_step <= 0) {
 746:         throw std::invalid_argument("match_step must be > 0");
 747:     }
 748:     if (dtw_window < 0) {
 749:         throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
 750:     }
 751:     if (cos_prefilter_top <= 0) {
 752:         throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
 753:     }
 754:     if (T_idx < L_query + M_forward + 10) return py::none();
 755:     if (T_idx - L_query + 1 < 0) return py::none();
 756: 
 757:     // 查询窗口标准化
 758:     auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
 759:     if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) return py::none();
 760: 
 761:     std::vector<double> query_rets;
 762:     {
 763:         py::gil_scoped_release release;
 764:         query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
 765:     }
 766:     if (query_rets.size() < 2) return py::none();
 767: 
 768:     py::ssize_t search_end = T_idx - L_query;
 769:     if (search_end < L_query) return py::none();
 770:     py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
 771:                                         py::ssize_t(T_idx - T_back));
 772: 
 773:     // ── 委托共享核心（无预计算缓存，现场标准化）──
 774:     std::optional<PatternResult> result_opt;
 775:     {
 776:         py::gil_scoped_release release;
 777:         result_opt = pattern_match_core(
 778:             prices, n_prices, T_idx, k, L_query, T_back,
 779:             match_step, M_forward, dtw_window, cos_prefilter_top,
 780:             query_rets, search_start, search_end,
 781:             nullptr  // 无预计算缓存
 782:         );
 783:     }
 784: 
 785:     if (!result_opt.has_value()) return py::none();
 786: 
 787:     // ── 构造返回值 ──
 788:     py::dict result;
 789:     result["top1_sim"] = result_opt->top1_sim;
 790:     result["top5_avg_sim"] = result_opt->top5_avg_sim;
 791:     result["sim_decay"] = result_opt->sim_decay;
 792:     result["sim_variance"] = result_opt->sim_variance;
 793:     result["match_distance_ratio"] = result_opt->match_distance_ratio;
 794:     result["avg_future_ret"] = result_opt->avg_future_ret;
 795:     result["weighted_future_ret"] = result_opt->weighted_future_ret;
 796:     result["median_future_ret"] = result_opt->median_future_ret;
 797:     result["ret_sign_consistency"] = result_opt->ret_sign_consistency;
 798:     result["best_match_ret"] = result_opt->best_match_ret;
 799:     result["max_dd_in_matches"] = result_opt->max_dd_in_matches;
 800:     result["match_time_span"] = result_opt->match_time_span;
 801:     result["match_time_span_ratio"] = result_opt->match_time_span_ratio;
 802:     result["match_cluster_ratio"] = result_opt->match_cluster_ratio;
 803:     result["n_matches_above_thresh"] = result_opt->n_matches_above_thresh;
 804:     return result;
 805: }
 806: 
 807: // ═══════════════════════════════════════════════════════════════
 808: // 第七部分: 批量形态匹配 (v3 新增)
 809: // ═══════════════════════════════════════════════════════════════
 810: 
 811: py::tuple pattern_match_batch(
 812:     ArrD prices_arr,
 813:     ArrI64 t_indices_arr,
 814:     int k = 10,
 815:     int L_query = 20,
 816:     int T_back = 750,
 817:     int match_step = 1,
 818:     int M_forward = 5,
 819:     int dtw_window = 5,
 820:     int cos_prefilter_top = 50
 821: ) {
 822:     auto prices_buf = prices_arr.unchecked<1>();
 823:     py::ssize_t n_prices = prices_buf.shape(0);
 824:     const double* prices = prices_buf.data(0);
 825: 
 826:     auto t_buf = t_indices_arr.unchecked<1>();
 827:     py::ssize_t n_samples = t_buf.shape(0);
 828:     const int64_t* t_ptr = t_buf.data(0);
 829: 
 830:     // ── 输入校验 ──
 831:     if (L_query < 3) {
 832:         throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
 833:     }
 834:     if (T_back <= 0) {
 835:         throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
 836:     }
 837:     if (k <= 0) {
 838:         throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
 839:     }
 840:     if (M_forward < 1) {
 841:         throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
 842:     }
 843:     if (match_step <= 0) {
 844:         throw std::invalid_argument("match_step must be > 0");
 845:     }
 846:     if (dtw_window < 0) {
 847:         throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
 848:     }
 849:     if (cos_prefilter_top <= 0) {
 850:         throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'src/cpp/etf_core.cpp' -Encoding UTF8; foreach ("'$range in @(@(472,620),@(621,713))) { Write-Host "--- lines $($range[0])-$($range[1]) ---"; for ($i=$range[0]-1; $i -lt [Math]::Min($range[1],$lines.Count); $i++) { '"'{0,4}: {1}' -f ("'$i+1), $lines[$i] } }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 238ms:
--- lines 472-620 ---
 472: // 从 Top-K 有效匹配中提取 15 维特征
 473: PatternResult compute_pattern_features_cpp(
 474:     const std::vector<double>& valid_scores,
 475:     const std::vector<double>& valid_frets,
 476:     const std::vector<py::ssize_t>& valid_ends,
 477:     int T_back
 478: ) {
 479:     PatternResult r{};
 480:     int top_k_actual = static_cast<int>(valid_scores.size());
 481: 
 482:     // F1-F5: 相似度特征
 483:     r.top1_sim = valid_scores[0];
 484:     int n_avg = std::min(5, top_k_actual);
 485:     double sum_avg = 0.0;
 486:     for (int i = 0; i < n_avg; ++i) sum_avg += valid_scores[i];
 487:     r.top5_avg_sim = sum_avg / n_avg;
 488:     r.sim_decay = r.top1_sim - r.top5_avg_sim;
 489: 
 490:     double var = 0.0, mean_s = 0.0;
 491:     for (auto s : valid_scores) mean_s += s;
 492:     mean_s /= top_k_actual;
 493:     for (auto s : valid_scores) var += (s - mean_s) * (s - mean_s);
 494:     r.sim_variance = (top_k_actual > 1) ? var / top_k_actual : 0.0;
 495:     r.match_distance_ratio = (r.top1_sim > 1e-12) ? r.sim_decay / r.top1_sim : 0.0;
 496: 
 497:     // F6-F11: 后续表现
 498:     double sum_fr = 0.0;
 499:     for (auto fr : valid_frets) sum_fr += fr;
 500:     r.avg_future_ret = sum_fr / top_k_actual;
 501: 
 502:     double sum_ws = 0.0, sum_w = 0.0;
 503:     for (int i = 0; i < top_k_actual; ++i) {
 504:         sum_ws += valid_scores[i] * valid_frets[i];
 505:         sum_w += valid_scores[i];
 506:     }
 507:     r.weighted_future_ret = (sum_w > 1e-12) ? sum_ws / sum_w : r.avg_future_ret;
 508: 
 509:     std::vector<double> sorted_fr = valid_frets;
 510:     std::sort(sorted_fr.begin(), sorted_fr.end());
 511:     r.median_future_ret = (top_k_actual % 2 == 1)
 512:         ? sorted_fr[top_k_actual / 2]
 513:         : (sorted_fr[top_k_actual / 2 - 1] + sorted_fr[top_k_actual / 2]) / 2.0;
 514: 
 515:     int pos_count = 0;
 516:     for (auto fr : valid_frets) if (fr > 0) ++pos_count;
 517:     r.ret_sign_consistency = static_cast<double>(pos_count) / top_k_actual;
 518:     r.best_match_ret = valid_frets[0];
 519: 
 520:     double min_fr = *std::min_element(valid_frets.begin(), valid_frets.end());
 521:     r.max_dd_in_matches = std::max(0.0, -min_fr);
 522: 
 523:     // F12-F15: 匹配质量
 524:     auto [min_e, max_e] = std::minmax_element(valid_ends.begin(), valid_ends.end());
 525:     r.match_time_span = static_cast<double>(*max_e - *min_e);
 526:     r.match_time_span_ratio = r.match_time_span / T_back;
 527: 
 528:     std::vector<py::ssize_t> sorted_ends = valid_ends;
 529:     std::sort(sorted_ends.begin(), sorted_ends.end());
 530:     int max_in_window = 0;
 531:     for (int i = 0; i < top_k_actual; ++i) {
 532:         double target = static_cast<double>(sorted_ends[i]) + 60.0;
 533:         auto it = std::upper_bound(sorted_ends.begin(), sorted_ends.end(),
 534:                                    static_cast<py::ssize_t>(target));
 535:         int count = static_cast<int>(it - sorted_ends.begin()) - i;
 536:         max_in_window = std::max(max_in_window, count);
 537:     }
 538:     r.match_cluster_ratio = static_cast<double>(max_in_window) / top_k_actual;
 539: 
 540:     int above = 0;
 541:     for (auto s : valid_scores) if (s > 0.8) ++above;
 542:     r.n_matches_above_thresh = above;
 543: 
 544:     return r;
 545: }
 546: 
 547: // ═══════════════════════════════════════════════════════════════
 548: // 共享核心：余弦预筛选 → DTW 精排 → 特征提取
 549: // single 和 batch 共用此函数，消除 ~400 行重复逻辑
 550: // ═══════════════════════════════════════════════════════════════
 551: std::optional<PatternResult> pattern_match_core(
 552:     const double* prices, py::ssize_t n_prices,
 553:     int T_idx, int k, int L_query, int T_back,
 554:     int match_step, int M_forward, int dtw_window,
 555:     int cos_prefilter_top,
 556:     const std::vector<double>& query_rets,
 557:     py::ssize_t search_start, py::ssize_t search_end,
 558:     const std::vector<std::vector<double>>* precomputed_rets
 559: ) {
 560:     py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());
 561: 
 562:     // ═══ 第1遍：余弦相似度 + 快速形状距离（全量候选）═══
 563:     std::vector<MatchCandidate> cos_candidates;
 564:     std::vector<double> fast_shape_dists;
 565: 
 566:     for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
 567:         py::ssize_t hist_start = hist_end - L_query + 1;
 568:         if (hist_start < 0) continue;
 569: 
 570:         // 获取标准化收益率：缓存优先，否则现场计算
 571:         const std::vector<double>* hist_rets_ptr = nullptr;
 572:         std::vector<double> hist_rets_scratch;
 573: 
 574:         if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size())) {
 575:             hist_rets_ptr = &(*precomputed_rets)[hist_end];
 576:         } else {
 577:             auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
 578:             if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
 579:                 hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query);
 580:                 hist_rets_ptr = &hist_rets_scratch;
 581:             }
 582:         }
 583: 
 584:         if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;
 585: 
 586:         const auto& hist_rets = *hist_rets_ptr;
 587: 
 588:         // 余弦相似度
 589:         double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
 590:         py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
 591:         for (py::ssize_t i = 0; i < min_len; ++i) {
 592:             dot += hist_rets[i] * query_rets[i];
 593:             nx2 += hist_rets[i] * hist_rets[i];
 594:             ny2 += query_rets[i] * query_rets[i];
 595:         }
 596:         double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
 597:         double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;
 598: 
 599:         // 快速形状距离
 600:         double fast_d2 = 0.0;
 601:         for (py::ssize_t i = 0; i < min_len; ++i) {
 602:             double diff = hist_rets[i] - query_rets[i];
 603:             fast_d2 += diff * diff;
 604:         }
 605:         fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));
 606: 
 607:         if (cos_s > 0) {
 608:             cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
 609:         }
 610:     }
 611: 
 612:     if (cos_candidates.size() < 3) return std::nullopt;
 613: 
 614:     // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
 615:     double sigma_fast = 1.0;
 616:     if (fast_shape_dists.size() > 1) {
 617:         double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0.0)
 618:                         / fast_shape_dists.size();
 619:         double var_fd = 0.0;
 620:         for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
--- lines 621-713 ---
 621:         var_fd /= fast_shape_dists.size();
 622:         sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)));
 623:     }
 624:     sigma_fast = std::max(sigma_fast, 1e-12);
 625: 
 626:     // 余弦排序 + 全量边界
 627:     std::sort(cos_candidates.begin(), cos_candidates.end(),
 628:               [](const MatchCandidate& a, const MatchCandidate& b) { return a.cos_s > b.cos_s; });
 629: 
 630:     double global_min_cos = cos_candidates.back().cos_s;
 631:     double global_max_cos = cos_candidates.front().cos_s;
 632: 
 633:     int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
 634:     cos_candidates.resize(n_cos);
 635: 
 636:     // ═══ 第2遍：DTW 精排 (仅 top-N) ═══
 637:     std::vector<double> dtw_dists, cos_sims, future_rets;
 638:     std::vector<py::ssize_t> match_ends;
 639:     dtw_dists.reserve(n_cos);
 640:     cos_sims.reserve(n_cos);
 641:     future_rets.reserve(n_cos);
 642:     match_ends.reserve(n_cos);
 643: 
 644:     for (const auto& cand : cos_candidates) {
 645:         py::ssize_t hn = static_cast<py::ssize_t>(cand.hist_rets.size());
 646:         double dtw_d = dtw_distance_span(cand.hist_rets.data(), hn,
 647:                                           query_rets.data(), n_query, dtw_window);
 648: 
 649:         dtw_dists.push_back(dtw_d);
 650:         cos_sims.push_back(cand.cos_s);
 651: 
 652:         py::ssize_t fut_end = cand.hist_end + M_forward;
 653:         if (fut_end < n_prices && fut_end < T_idx) {
 654:             future_rets.push_back(prices[fut_end] / prices[cand.hist_end] - 1.0);
 655:         } else {
 656:             future_rets.push_back(std::numeric_limits<double>::quiet_NaN());
 657:         }
 658:         match_ends.push_back(cand.hist_end);
 659:     }
 660: 
 661:     if (dtw_dists.size() < 3) return std::nullopt;
 662: 
 663:     // sim_dtw = exp(-dtw/sigma)
 664:     double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;
 665: 
 666:     std::vector<double> sim_dtw(dtw_dists.size());
 667:     double min_dtw_v = std::numeric_limits<double>::max();
 668:     double max_dtw_v = std::numeric_limits<double>::lowest();
 669:     for (size_t i = 0; i < dtw_dists.size(); ++i) {
 670:         sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
 671:         min_dtw_v = std::min(min_dtw_v, sim_dtw[i]);
 672:         max_dtw_v = std::max(max_dtw_v, sim_dtw[i]);
 673:     }
 674: 
 675:     // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
 676:     double range_dtw = (max_dtw_v - min_dtw_v > 1e-12) ? (max_dtw_v - min_dtw_v) : 1.0;
 677:     double range_cos_val = (global_max_cos - global_min_cos > 1e-12)
 678:                            ? (global_max_cos - global_min_cos) : 1.0;
 679: 
 680:     struct Scored { double score, fut_ret; py::ssize_t end_idx; };
 681:     std::vector<Scored> scored;
 682:     scored.reserve(sim_dtw.size());
 683:     for (size_t i = 0; i < sim_dtw.size(); ++i) {
 684:         double nd = (sim_dtw[i] - min_dtw_v) / range_dtw;
 685:         double nc = (cos_sims[i] - global_min_cos) / range_cos_val;
 686:         scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
 687:     }
 688: 
 689:     std::sort(scored.begin(), scored.end(),
 690:               [](const Scored& a, const Scored& b) { return a.score > b.score; });
 691: 
 692:     int top_k = std::min(k, static_cast<int>(scored.size()));
 693: 
 694:     // 过滤 NaN 未来收益
 695:     std::vector<double> valid_scores, valid_frets;
 696:     std::vector<py::ssize_t> valid_ends;
 697:     for (int i = 0; i < top_k; ++i) {
 698:         if (!std::isnan(scored[i].fut_ret)) {
 699:             valid_scores.push_back(scored[i].score);
 700:             valid_frets.push_back(scored[i].fut_ret);
 701:             valid_ends.push_back(scored[i].end_idx);
 702:         }
 703:     }
 704:     if (valid_scores.size() < 2) return std::nullopt;
 705: 
 706:     return compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);
 707: }
 708: 
 709: } // namespace
 710: 
 711: // ═══════════════════════════════════════════════════════════════
 712: // 第六部分-A: 单点形态匹配（薄包装 → pattern_match_core）
 713: // ═══════════════════════════════════════════════════════════════

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'src/cpp/etf_core.cpp' -Encoding UTF8; for ("'$i=565; $i -lt 626; $i++) { '"'{0,4}: {1}' -f ("'$i+1), $lines[$i] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 152ms:
 566:     for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
 567:         py::ssize_t hist_start = hist_end - L_query + 1;
 568:         if (hist_start < 0) continue;
 569: 
 570:         // 获取标准化收益率：缓存优先，否则现场计算
 571:         const std::vector<double>* hist_rets_ptr = nullptr;
 572:         std::vector<double> hist_rets_scratch;
 573: 
 574:         if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size())) {
 575:             hist_rets_ptr = &(*precomputed_rets)[hist_end];
 576:         } else {
 577:             auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
 578:             if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
 579:                 hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query);
 580:                 hist_rets_ptr = &hist_rets_scratch;
 581:             }
 582:         }
 583: 
 584:         if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;
 585: 
 586:         const auto& hist_rets = *hist_rets_ptr;
 587: 
 588:         // 余弦相似度
 589:         double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
 590:         py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
 591:         for (py::ssize_t i = 0; i < min_len; ++i) {
 592:             dot += hist_rets[i] * query_rets[i];
 593:             nx2 += hist_rets[i] * hist_rets[i];
 594:             ny2 += query_rets[i] * query_rets[i];
 595:         }
 596:         double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
 597:         double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;
 598: 
 599:         // 快速形状距离
 600:         double fast_d2 = 0.0;
 601:         for (py::ssize_t i = 0; i < min_len; ++i) {
 602:             double diff = hist_rets[i] - query_rets[i];
 603:             fast_d2 += diff * diff;
 604:         }
 605:         fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));
 606: 
 607:         if (cos_s > 0) {
 608:             cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
 609:         }
 610:     }
 611: 
 612:     if (cos_candidates.size() < 3) return std::nullopt;
 613: 
 614:     // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
 615:     double sigma_fast = 1.0;
 616:     if (fast_shape_dists.size() > 1) {
 617:         double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0.0)
 618:                         / fast_shape_dists.size();
 619:         double var_fd = 0.0;
 620:         for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
 621:         var_fd /= fast_shape_dists.size();
 622:         sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)));
 623:     }
 624:     sigma_fast = std::max(sigma_fast, 1e-12);
 625: 
 626:     // 余弦排序 + 全量边界

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'src/cpp/etf_core.cpp' -Encoding UTF8; for ("'$i=713; $i -lt 811; $i++) { '"'{0,4}: {1}' -f ("'$i+1), $lines[$i] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 156ms:
 714: py::object pattern_match_single(
 715:     ArrD prices_arr,
 716:     int T_idx,
 717:     int k = 10,
 718:     int L_query = 20,
 719:     int T_back = 750,
 720:     int match_step = 1,
 721:     int M_forward = 5,
 722:     int dtw_window = 5,
 723:     int cos_prefilter_top = 50
 724: ) {
 725:     auto prices_buf = prices_arr.unchecked<1>();
 726:     py::ssize_t n_prices = prices_buf.shape(0);
 727:     const double* prices = prices_buf.data(0);
 728: 
 729:     // ── 输入校验 ──
 730:     if (T_idx < 0 || static_cast<py::ssize_t>(T_idx) >= n_prices) {
 731:         throw std::out_of_range("T_idx must satisfy 0 <= T_idx < len(prices), got " + std::to_string(T_idx));
 732:     }
 733:     if (L_query < 3) {
 734:         throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
 735:     }
 736:     if (T_back <= 0) {
 737:         throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
 738:     }
 739:     if (k <= 0) {
 740:         throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
 741:     }
 742:     if (M_forward < 1) {
 743:         throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
 744:     }
 745:     if (match_step <= 0) {
 746:         throw std::invalid_argument("match_step must be > 0");
 747:     }
 748:     if (dtw_window < 0) {
 749:         throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
 750:     }
 751:     if (cos_prefilter_top <= 0) {
 752:         throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
 753:     }
 754:     if (T_idx < L_query + M_forward + 10) return py::none();
 755:     if (T_idx - L_query + 1 < 0) return py::none();
 756: 
 757:     // 查询窗口标准化
 758:     auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
 759:     if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) return py::none();
 760: 
 761:     std::vector<double> query_rets;
 762:     {
 763:         py::gil_scoped_release release;
 764:         query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
 765:     }
 766:     if (query_rets.size() < 2) return py::none();
 767: 
 768:     py::ssize_t search_end = T_idx - L_query;
 769:     if (search_end < L_query) return py::none();
 770:     py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
 771:                                         py::ssize_t(T_idx - T_back));
 772: 
 773:     // ── 委托共享核心（无预计算缓存，现场标准化）──
 774:     std::optional<PatternResult> result_opt;
 775:     {
 776:         py::gil_scoped_release release;
 777:         result_opt = pattern_match_core(
 778:             prices, n_prices, T_idx, k, L_query, T_back,
 779:             match_step, M_forward, dtw_window, cos_prefilter_top,
 780:             query_rets, search_start, search_end,
 781:             nullptr  // 无预计算缓存
 782:         );
 783:     }
 784: 
 785:     if (!result_opt.has_value()) return py::none();
 786: 
 787:     // ── 构造返回值 ──
 788:     py::dict result;
 789:     result["top1_sim"] = result_opt->top1_sim;
 790:     result["top5_avg_sim"] = result_opt->top5_avg_sim;
 791:     result["sim_decay"] = result_opt->sim_decay;
 792:     result["sim_variance"] = result_opt->sim_variance;
 793:     result["match_distance_ratio"] = result_opt->match_distance_ratio;
 794:     result["avg_future_ret"] = result_opt->avg_future_ret;
 795:     result["weighted_future_ret"] = result_opt->weighted_future_ret;
 796:     result["median_future_ret"] = result_opt->median_future_ret;
 797:     result["ret_sign_consistency"] = result_opt->ret_sign_consistency;
 798:     result["best_match_ret"] = result_opt->best_match_ret;
 799:     result["max_dd_in_matches"] = result_opt->max_dd_in_matches;
 800:     result["match_time_span"] = result_opt->match_time_span;
 801:     result["match_time_span_ratio"] = result_opt->match_time_span_ratio;
 802:     result["match_cluster_ratio"] = result_opt->match_cluster_ratio;
 803:     result["n_matches_above_thresh"] = result_opt->n_matches_above_thresh;
 804:     return result;
 805: }
 806: 
 807: // ═══════════════════════════════════════════════════════════════
 808: // 第七部分: 批量形态匹配 (v3 新增)
 809: // ═══════════════════════════════════════════════════════════════
 810: 
 811: py::tuple pattern_match_batch(

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'src/cpp/etf_core.cpp' -Encoding UTF8; foreach ("'$range in @(@(811,940),@(941,1083))) { Write-Host "--- lines $($range[0])-$($range[1]) ---"; for ($i=$range[0]-1; $i -lt [Math]::Min($range[1],$lines.Count); $i++) { '"'{0,4}: {1}' -f ("'$i+1), $lines[$i] } }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 212ms:
--- lines 811-940 ---
 811: py::tuple pattern_match_batch(
 812:     ArrD prices_arr,
 813:     ArrI64 t_indices_arr,
 814:     int k = 10,
 815:     int L_query = 20,
 816:     int T_back = 750,
 817:     int match_step = 1,
 818:     int M_forward = 5,
 819:     int dtw_window = 5,
 820:     int cos_prefilter_top = 50
 821: ) {
 822:     auto prices_buf = prices_arr.unchecked<1>();
 823:     py::ssize_t n_prices = prices_buf.shape(0);
 824:     const double* prices = prices_buf.data(0);
 825: 
 826:     auto t_buf = t_indices_arr.unchecked<1>();
 827:     py::ssize_t n_samples = t_buf.shape(0);
 828:     const int64_t* t_ptr = t_buf.data(0);
 829: 
 830:     // ── 输入校验 ──
 831:     if (L_query < 3) {
 832:         throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
 833:     }
 834:     if (T_back <= 0) {
 835:         throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
 836:     }
 837:     if (k <= 0) {
 838:         throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
 839:     }
 840:     if (M_forward < 1) {
 841:         throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
 842:     }
 843:     if (match_step <= 0) {
 844:         throw std::invalid_argument("match_step must be > 0");
 845:     }
 846:     if (dtw_window < 0) {
 847:         throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
 848:     }
 849:     if (cos_prefilter_top <= 0) {
 850:         throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
 851:     }
 852:     if (n_samples == 0) {
 853:         ArrD empty_features(std::vector<py::ssize_t>{0, 15});
 854:         py::array_t<bool> empty_mask(std::vector<py::ssize_t>{0});
 855:         return py::make_tuple(empty_features, empty_mask);
 856:     }
 857: 
 858:     for (py::ssize_t i = 1; i < n_samples; ++i) {
 859:         if (t_ptr[i] <= t_ptr[i - 1]) {
 860:             throw std::invalid_argument("t_indices must be strictly increasing");
 861:         }
 862:     }
 863:     if (t_ptr[n_samples - 1] >= n_prices) {
 864:         throw std::invalid_argument("max(t_indices) must be < len(prices)");
 865:     }
 866: 
 867:     std::vector<double> features_flat;
 868:     features_flat.reserve(n_samples * 15);
 869:     std::vector<bool> valid_mask(n_samples, false);
 870: 
 871:     {
 872:         // ── GIL 释放区：纯 C++ 批量计算 ──
 873:         py::gil_scoped_release release;
 874: 
 875:         // ── 第一遍：计算所有 T_idx 搜索范围的并集（避免预计算无用窗口）──
 876:         py::ssize_t precompute_start = n_prices;
 877:         py::ssize_t precompute_end = 0;
 878:         for (py::ssize_t s = 0; s < n_samples; ++s) {
 879:             int T_idx = static_cast<int>(t_ptr[s]);
 880:             if (T_idx < L_query + M_forward + 10) continue;
 881:             py::ssize_t s_end = T_idx - L_query;
 882:             if (s_end < L_query) continue;
 883:             py::ssize_t s_start = std::max(py::ssize_t(L_query - 1),
 884:                                            py::ssize_t(T_idx - T_back));
 885:             if (s_start < s_end) {
 886:                 precompute_start = std::min(precompute_start, s_start);
 887:                 precompute_end = std::max(precompute_end, s_end);
 888:             }
 889:         }
 890: 
 891:         // ── 仅预计算搜索范围并集内的窗口标准化收益率 ──
 892:         std::vector<std::vector<double>> precomputed_rets(n_prices);
 893:         if (precompute_start <= precompute_end) {
 894:             for (py::ssize_t end = precompute_start; end <= precompute_end; ++end) {
 895:                 py::ssize_t start = end - L_query + 1;
 896:                 if (start >= 0) {
 897:                     auto window_prices = extract_window(prices, start, end);
 898:                     precomputed_rets[end] = standardize_returns_cpp(window_prices.data(), L_query);
 899:                 }
 900:             }
 901:         }
 902: 
 903:         // ── 对每个 T_idx 执行形态匹配（复用预计算缓存）──
 904:         for (py::ssize_t s = 0; s < n_samples; ++s) {
 905:             int T_idx = static_cast<int>(t_ptr[s]);
 906: 
 907:             if (T_idx < L_query + M_forward + 10) continue;
 908:             if (T_idx - L_query + 1 < 0) continue;
 909: 
 910:             auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
 911:             if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) continue;
 912: 
 913:             auto query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
 914:             if (query_rets.size() < 2) continue;
 915: 
 916:             py::ssize_t search_end = T_idx - L_query;
 917:             if (search_end < L_query) continue;
 918:             py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
 919:                                                 py::ssize_t(T_idx - T_back));
 920: 
 921:             // ── 委托共享核心（使用预计算缓存）──
 922:             auto result_opt = pattern_match_core(
 923:                 prices, n_prices, T_idx, k, L_query, T_back,
 924:                 match_step, M_forward, dtw_window, cos_prefilter_top,
 925:                 query_rets, search_start, search_end,
 926:                 &precomputed_rets
 927:             );
 928: 
 929:             if (!result_opt.has_value()) continue;
 930: 
 931:             auto& r = *result_opt;
 932:             features_flat.push_back(r.top1_sim);
 933:             features_flat.push_back(r.top5_avg_sim);
 934:             features_flat.push_back(r.sim_decay);
 935:             features_flat.push_back(r.sim_variance);
 936:             features_flat.push_back(r.match_distance_ratio);
 937:             features_flat.push_back(r.avg_future_ret);
 938:             features_flat.push_back(r.weighted_future_ret);
 939:             features_flat.push_back(r.median_future_ret);
 940:             features_flat.push_back(r.ret_sign_consistency);
--- lines 941-1083 ---
 941:             features_flat.push_back(r.best_match_ret);
 942:             features_flat.push_back(r.max_dd_in_matches);
 943:             features_flat.push_back(r.match_time_span);
 944:             features_flat.push_back(r.match_time_span_ratio);
 945:             features_flat.push_back(r.match_cluster_ratio);
 946:             features_flat.push_back(static_cast<double>(r.n_matches_above_thresh));
 947: 
 948:             valid_mask[s] = true;
 949:         }
 950:     } // GIL 在此重新获取
 951: 
 952:     // ── 构造返回数组 ──
 953:     py::ssize_t n_valid = static_cast<py::ssize_t>(features_flat.size()) / 15;
 954:     ArrD features_X15(std::vector<py::ssize_t>{n_valid, 15});
 955:     auto fx_buf = features_X15.mutable_unchecked<2>();
 956:     for (py::ssize_t i = 0; i < n_valid; ++i) {
 957:         for (py::ssize_t j = 0; j < 15; ++j) {
 958:             fx_buf(i, j) = features_flat[i * 15 + j];
 959:         }
 960:     }
 961: 
 962:     py::array_t<bool> valid_mask_arr(std::vector<py::ssize_t>{n_samples});
 963:     auto vm_buf = valid_mask_arr.mutable_unchecked<1>();
 964:     for (py::ssize_t i = 0; i < n_samples; ++i) {
 965:         vm_buf(i) = valid_mask[i];
 966:     }
 967: 
 968:     return py::make_tuple(features_X15, valid_mask_arr);
 969: }
 970: 
 971: // ═══════════════════════════════════════════════════════════════
 972: // 模块定义
 973: // ═══════════════════════════════════════════════════════════════
 974: 
 975: PYBIND11_MODULE(etf_core, m) {
 976:     m.doc() = "ETF pattern matching core — C++ accelerated (pybind11)\n\n"
 977:               "来源: 形态匹配ETF组合策略_V3.3.py\n"
 978:               "模块: dtw_distance, standardize_returns, cosine_similarity,\n"
 979:               "       compute_adx, compute_atr, dtw_distance_batch,\n"
 980:               "       pattern_match_single, pattern_match_batch\n"
 981:               "v2: 三模块合并为单一 etf_core, /utf-8, py::ssize_t, forcecast\n"
 982:               "v3: 新增 pattern_match_batch，支持同 ETF 多 T_idx 批量形态匹配";
 983: 
 984:     // ── 序列预处理 ──
 985:     m.def("standardize_returns", &standardize_returns,
 986:           py::arg("price_series"),
 987:           "计算标准化收益率序列: (rets - mean) / std.\n\n"
 988:           "Args: price_series (1-D float64 array, n>=2)\n"
 989:           "Returns: 1-D float64 array (length n-1)");
 990: 
 991:     m.def("cosine_similarity", &cosine_similarity,
 992:           py::arg("x"), py::arg("y"),
 993:           "两向量余弦相似度 ∈ [-1, 1].\n"
 994:           "norm < 1e-12 时返回 0.0.");
 995: 
 996:     // ── DTW ──
 997:     m.def("dtw_distance", &dtw_distance,
 998:           py::arg("x"), py::arg("y"), py::arg("window") = 5,
 999:           "Sakoe-Chiba band DTW 距离.\n"
1000:           "返回归一化距离: sqrt(dtw[n,m]) / (n+m).\n"
1001:           "空序列返回 inf.");
1002: 
1003:     m.def("dtw_distance_batch", &dtw_distance_batch,
1004:           py::arg("query"), py::arg("candidates"),
1005:           py::arg("window") = 5, py::arg("top_k") = 0,
1006:           "批量 DTW: 一个 query 对 N 个 candidates.\n\n"
1007:           "Args:\n"
1008:           "  query: 1-D float64 array (L,)\n"
1009:           "  candidates: 2-D float64 array (N, L)\n"
1010:           "  window: Sakoe-Chiba band 宽度\n"
1011:           "  top_k: 若 >0 且 <N，返回 (top_indices, top_distances);\n"
1012:           "         否则返回全部 distances (N,)\n\n"
1013:           "Returns: distances (N,) 或 (indices, distances) 各 (top_k,)");
1014: 
1015:     // ── 技术指标 ──
1016:     m.def("compute_adx", &compute_adx,
1017:           py::arg("high"), py::arg("low"), py::arg("close"),
1018:           py::arg("n") = 14,
1019:           "ADX (Average Directional Index), Wilder's smoothing.\n"
1020:           "数据不足时返回 25.0 (中性值).");
1021: 
1022:     m.def("compute_atr", &compute_atr,
1023:           py::arg("high"), py::arg("low"), py::arg("close"),
1024:           py::arg("n") = 14,
1025:           "ATR (Average True Range).\n"
1026:           "前 n 天为 NaN.");
1027: 
1028:     // 模块常量：15 维特征名（顺序与 pattern_match_batch 的 features_X15 列一致）
1029:     m.attr("FEATURE_KEYS") = py::make_tuple(
1030:         "top1_sim",
1031:         "top5_avg_sim",
1032:         "sim_decay",
1033:         "sim_variance",
1034:         "match_distance_ratio",
1035:         "avg_future_ret",
1036:         "weighted_future_ret",
1037:         "median_future_ret",
1038:         "ret_sign_consistency",
1039:         "best_match_ret",
1040:         "max_dd_in_matches",
1041:         "match_time_span",
1042:         "match_time_span_ratio",
1043:         "match_cluster_ratio",
1044:         "n_matches_above_thresh"
1045:     );
1046: 
1047:     // ── 形态匹配 ──
1048:     m.def("pattern_match_single", &pattern_match_single,
1049:           py::arg("prices"),
1050:           py::arg("T_idx"),
1051:           py::arg("k") = 10,
1052:           py::arg("L_query") = 20,
1053:           py::arg("T_back") = 750,
1054:           py::arg("match_step") = 1,
1055:           py::arg("M_forward") = 5,
1056:           py::arg("dtw_window") = 5,
1057:           py::arg("cos_prefilter_top") = 50,
1058:           "单 ETF 单时点形态匹配 → 15维特征字典.\n\n"
1059:           "V3.0 余弦预筛选: 第1遍全量余弦 → 第2遍 DTW 精排.\n"
1060:           "前视偏差防护: fut_end < T_idx 严格约束.\n"
1061:           "数据不足返回 None.\n\n"
1062:           "Returns: dict with 15 keys or None.\n"
1063:           "  F1-F5:  top1_sim, top5_avg_sim, sim_decay, sim_variance, match_distance_ratio\n"
1064:           "  F6-F11: avg_future_ret, weighted_future_ret, median_future_ret,\n"
1065:           "          ret_sign_consistency, best_match_ret, max_dd_in_matches\n"
1066:           "  F12-F15: match_time_span, match_time_span_ratio, match_cluster_ratio,\n"
1067:           "           n_matches_above_thresh");
1068: 
1069:     m.def("pattern_match_batch", &pattern_match_batch,
1070:           py::arg("prices"), py::arg("t_indices"),
1071:           py::arg("k") = 10, py::arg("L_query") = 20,
1072:           py::arg("T_back") = 750, py::arg("match_step") = 1,
1073:           py::arg("M_forward") = 5, py::arg("dtw_window") = 5,
1074:           py::arg("cos_prefilter_top") = 50,
1075:           "批量形态匹配——同ETF多T_idx.\n\n"
1076:           "核心优化: 候选窗口标准化收益率在相邻 T_idx 之间高度重叠，\n"
1077:           "C++ 内部一次性预计算并复用，避免 Python 往返和重复标准化.\n\n"
1078:           "Returns: (features_X15, valid_mask).\n"
1079:           "features_X15: (n_valid, 15) float64 — 仅有效样本.\n"
1080:           "valid_mask: (n_samples,) bool.\n"
1081:           "feature_keys 已提升为模块常量 etf_core.FEATURE_KEYS (15 str).");
1082: }

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'src/cpp/etf_core.cpp' -Encoding UTF8; for ("'$i=915; $i -lt 985; $i++) { '"'{0,4}: {1}' -f ("'$i+1), $lines[$i] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 159ms:
 916:             py::ssize_t search_end = T_idx - L_query;
 917:             if (search_end < L_query) continue;
 918:             py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
 919:                                                 py::ssize_t(T_idx - T_back));
 920: 
 921:             // ── 委托共享核心（使用预计算缓存）──
 922:             auto result_opt = pattern_match_core(
 923:                 prices, n_prices, T_idx, k, L_query, T_back,
 924:                 match_step, M_forward, dtw_window, cos_prefilter_top,
 925:                 query_rets, search_start, search_end,
 926:                 &precomputed_rets
 927:             );
 928: 
 929:             if (!result_opt.has_value()) continue;
 930: 
 931:             auto& r = *result_opt;
 932:             features_flat.push_back(r.top1_sim);
 933:             features_flat.push_back(r.top5_avg_sim);
 934:             features_flat.push_back(r.sim_decay);
 935:             features_flat.push_back(r.sim_variance);
 936:             features_flat.push_back(r.match_distance_ratio);
 937:             features_flat.push_back(r.avg_future_ret);
 938:             features_flat.push_back(r.weighted_future_ret);
 939:             features_flat.push_back(r.median_future_ret);
 940:             features_flat.push_back(r.ret_sign_consistency);
 941:             features_flat.push_back(r.best_match_ret);
 942:             features_flat.push_back(r.max_dd_in_matches);
 943:             features_flat.push_back(r.match_time_span);
 944:             features_flat.push_back(r.match_time_span_ratio);
 945:             features_flat.push_back(r.match_cluster_ratio);
 946:             features_flat.push_back(static_cast<double>(r.n_matches_above_thresh));
 947: 
 948:             valid_mask[s] = true;
 949:         }
 950:     } // GIL 在此重新获取
 951: 
 952:     // ── 构造返回数组 ──
 953:     py::ssize_t n_valid = static_cast<py::ssize_t>(features_flat.size()) / 15;
 954:     ArrD features_X15(std::vector<py::ssize_t>{n_valid, 15});
 955:     auto fx_buf = features_X15.mutable_unchecked<2>();
 956:     for (py::ssize_t i = 0; i < n_valid; ++i) {
 957:         for (py::ssize_t j = 0; j < 15; ++j) {
 958:             fx_buf(i, j) = features_flat[i * 15 + j];
 959:         }
 960:     }
 961: 
 962:     py::array_t<bool> valid_mask_arr(std::vector<py::ssize_t>{n_samples});
 963:     auto vm_buf = valid_mask_arr.mutable_unchecked<1>();
 964:     for (py::ssize_t i = 0; i < n_samples; ++i) {
 965:         vm_buf(i) = valid_mask[i];
 966:     }
 967: 
 968:     return py::make_tuple(features_X15, valid_mask_arr);
 969: }
 970: 
 971: // ═══════════════════════════════════════════════════════════════
 972: // 模块定义
 973: // ═══════════════════════════════════════════════════════════════
 974: 
 975: PYBIND11_MODULE(etf_core, m) {
 976:     m.doc() = "ETF pattern matching core — C++ accelerated (pybind11)\n\n"
 977:               "来源: 形态匹配ETF组合策略_V3.3.py\n"
 978:               "模块: dtw_distance, standardize_returns, cosine_similarity,\n"
 979:               "       compute_adx, compute_atr, dtw_distance_batch,\n"
 980:               "       pattern_match_single, pattern_match_batch\n"
 981:               "v2: 三模块合并为单一 etf_core, /utf-8, py::ssize_t, forcecast\n"
 982:               "v3: 新增 pattern_match_batch，支持同 ETF 多 T_idx 批量形态匹配";
 983: 
 984:     // ── 序列预处理 ──
 985:     m.def("standardize_returns", &standardize_returns,

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Host '"'--- tests/test_dtw.py ---'; Get-Content -LiteralPath 'tests/test_dtw.py' -Raw -Encoding UTF8; Write-Host '--- tests/test_technical.py ---'; Get-Content -LiteralPath 'tests/test_technical.py' -Raw -Encoding UTF8; Write-Host '--- tests/test_pattern_match.py ---'; Get-Content -LiteralPath 'tests/test_pattern_match.py' -Raw -Encoding UTF8" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 180ms:
--- tests/test_dtw.py ---
# -*- coding: utf-8 -*-
"""DTW 模块测试 — 与原始 V3.3.py 实现交叉验证
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> v2 新增: NaN 边界测试 + cosine 阈值测试 (GPT-5.5 完备性审查 P1)"""


import sys
import os
import numpy as np
import pytest

# 添加 src 到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from core.dtw import (
    standardize_returns,
    cosine_similarity,
    dtw_distance,
    dtw_distance_batch,
    generate_query_candidates,
)


class TestStandardizeReturns:
    """standardize_returns 正确性测试"""

    def test_normal_case(self):
        """正常价格序列 — 应输出零均值、单位标准差的序列"""
        prices = np.array([100.0, 101.0, 102.5, 99.8, 103.2, 105.0])
        result = standardize_returns(prices)
        assert len(result) == 5  # n-1
        assert abs(np.mean(result)) < 1e-10  # 零均值
        assert abs(np.std(result) - 1.0) < 1e-10  # 单位标准差

    def test_constant_prices(self):
        """恒定价格 — std=0 时应返回去均值（零向量）序列"""
        prices = np.array([100.0, 100.0, 100.0, 100.0])
        result = standardize_returns(prices)
        assert len(result) == 3
        assert np.allclose(result, 0.0)

    def test_short_series(self):
        """少于2个元素 — 返回零数组"""
        result = standardize_returns(np.array([100.0]))
        assert len(result) == 0

    def test_zero_price_handling(self):
        """价格为0时应被 clip 到 1e-12"""
        prices = np.array([0.0, 100.0, 200.0])
        result = standardize_returns(prices)
        assert not np.any(np.isnan(result))
        assert not np.any(np.isinf(result))

    def test_nan_in_prices(self):
        """含 NaN 的价格 — NaN 收益率应被过滤"""
        # log(0) = -inf → diff 可能产生 nan
        prices = np.array([100.0, 100.0, 100.0, 100.0, 100.0])
        # 模拟: 在实际中 standardize_returns 中 np.diff(np.log(...))
        # 对恒定价格返回全零，不会有 NaN
        result = standardize_returns(prices)
        assert len(result) == 4
        assert not np.any(np.isnan(result))

    # v2 新增: 真实 NaN 边界测试 (GPT-5.5 完备性审查 P1)
    # 2026-07-12 修订: standardize_returns 已改为窗口级非有限值检查，
    # 任一价格为 NaN/Inf 即返回空数组，因此以下测试改为验证新契约。
    def test_nan_value_in_array(self):
        """数组中含 np.nan — 窗口级检查应返回空数组"""
        result = standardize_returns(np.array([100.0, np.nan, 101.0]))
        assert len(result) == 0

    def test_all_nan(self):
        """全 NaN — 窗口级检查应返回空数组"""
        result = standardize_returns(np.array([np.nan, np.nan]))
        assert len(result) == 0

    def test_zero_then_valid(self):
        """价格为0后被clip — 验证clip不产生NaN"""
        result = standardize_returns(np.array([0.0, 50.0, 100.0]))
        assert len(result) == 2
        assert not np.any(np.isnan(result))


class TestCosineSimilarity:
    """cosine_similarity 正确性测试"""

    def test_identical_vectors(self):
        x = np.array([1.0, 2.0, 3.0])
        assert cosine_similarity(x, x) == pytest.approx(1.0)

    def test_opposite_vectors(self):
        x = np.array([1.0, 2.0, 3.0])
        assert cosine_similarity(x, -x) == pytest.approx(-1.0)

    def test_orthogonal_vectors(self):
        x = np.array([1.0, 0.0, 0.0])
        y = np.array([0.0, 1.0, 0.0])
        assert cosine_similarity(x, y) == pytest.approx(0.0)

    def test_zero_vector(self):
        x = np.array([0.0, 0.0, 0.0])
        y = np.array([1.0, 2.0, 3.0])
        assert cosine_similarity(x, y) == 0.0
        assert cosine_similarity(y, x) == 0.0

    def test_near_zero_norm(self):
        """极小的 norm 应安全返回 0"""
        x = np.array([1e-13, 1e-13])
        y = np.array([1.0, 2.0])
        assert cosine_similarity(x, y) == 0.0

    # v2 新增: 阈值边界测试 (GPT-5.5 完备性审查 P1)
    def test_exactly_at_threshold(self):
        """norm 恰好等于 1e-12 — 不应返回 0（原逻辑用 < 而非 <=）"""
        x = np.array([1e-12, 0.0])
        y = np.array([1.0, 0.0])
        # norm_x = 1e-12, 不小于 1e-12 → 进入 dot/norm 计算
        result = cosine_similarity(x, y)
        assert result == pytest.approx(1.0)  # 方向完全一致


class TestDTWDistance:
    """DTW 距离正确性测试"""

    def test_identical_sequences(self):
        """相同序列的 DTW 距离应为 0"""
        x = np.array([0.1, 0.2, -0.1, 0.05, 0.0] * 4)  # L=20
        d = dtw_distance(x, x, window=5)
        assert d == pytest.approx(0.0, abs=1e-12)

    def test_same_length_sequences(self):
        """等长序列的基本 DTW 计算"""
        x = np.array([1.0, 2.0, 3.0, 2.0, 1.0])
        y = np.array([1.0, 2.0, 2.0, 3.0, 1.0])
        d = dtw_distance(x, y, window=5)
        assert d > 0
        assert not np.isnan(d)
        assert not np.isinf(d)

    def test_different_length_sequences(self):
        """不同长度序列"""
        x = np.array([0.1, -0.2, 0.3] * 5)   # L=15
        y = np.array([0.1, -0.2, 0.3] * 7)   # L=21
        d = dtw_distance(x, y, window=5)
        assert d >= 0
        assert not np.isnan(d)
        assert not np.isinf(d)

    def test_window_constraint(self):
        """band 约束应限制搜索范围"""
        x = np.random.randn(20)
        y = np.random.randn(20)
        d_narrow = dtw_distance(x, y, window=2)
        d_wide = dtw_distance(x, y, window=10)
        # 窄 band 距离应 ≥ 宽 band（因为搜索空间更受限）
        assert d_narrow >= d_wide - 1e-12

    def test_empty_input(self):
        """空序列应返回 inf"""
        assert dtw_distance(np.array([]), np.array([1.0, 2.0])) == np.inf
        assert dtw_distance(np.array([1.0, 2.0]), np.array([])) == np.inf

    def test_single_element(self):
        """单元素序列"""
        d = dtw_distance(np.array([0.5]), np.array([0.5]))
        assert d == pytest.approx(0.0, abs=1e-12)


class TestDTWDistanceBatch:
    """批量 DTW 测试"""

    def test_basic_batch(self):
        query = np.random.randn(20)
        candidates = np.random.randn(100, 20)
        distances = dtw_distance_batch(query, candidates, window=5)
        assert len(distances) == 100
        assert np.all(distances >= 0)

    def test_top_k(self):
        query = np.random.randn(20)
        candidates = np.random.randn(50, 20)
        idx, dists = dtw_distance_batch(query, candidates, window=5, top_k=10)
        assert len(idx) == 10
        assert len(dists) == 10
        # 确认排序
        assert np.all(np.diff(dists) >= 0)

    def test_consistency_with_single(self):
        """批量结果应与逐个调用一致"""
        query = np.random.randn(20)
        candidates = np.random.randn(30, 20)
        batch_dists = dtw_distance_batch(query, candidates, window=5)
        single_dists = np.array([dtw_distance(query, c, window=5) for c in candidates])
        assert np.allclose(batch_dists, single_dists)

    def test_empty_candidates(self):
        result = dtw_distance_batch(np.array([1.0]), np.empty((0, 1)))
        assert len(result) == 0

    def test_mismatched_lengths(self):
        with pytest.raises(ValueError):
            dtw_distance_batch(
                np.array([1.0, 2.0]),
                np.random.randn(10, 5),  # 列数不匹配
            )


class TestGenerateQueryCandidates:
    """查询/候选窗口生成测试"""

    def test_basic_generation(self):
        prices = np.sin(np.linspace(0, 10 * np.pi, 500)) + 10.0
        T_idx = 400
        q, cands, ends = generate_query_candidates(prices, T_idx, L_query=20)
        assert len(q) == 20
        assert cands.shape[1] == 20
        assert cands.shape[0] >= 300  # ~380 candidates
        # 前视偏差防护: 所有候选窗口结束索引 <= T_idx - L_query (=380)
        assert np.all(ends <= T_idx - 20)

    def test_insufficient_data(self):
        prices = np.array([100.0] * 10)
        with pytest.raises(ValueError):
            generate_query_candidates(prices, T_idx=5, L_query=20)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

--- tests/test_technical.py ---
# -*- coding: utf-8 -*-
"""技术指标模块测试
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "build", "Release"))

from core.technical import compute_adx, compute_sector_rotation, compute_atr


class TestComputeADX:
    """ADX 计算正确性测试"""

    def test_insufficient_data(self):
        """数据不足时返回中性值 25.0"""
        high = np.random.randn(20) + 100
        low = high - 2
        close = (high + low) / 2
        # n=14, 需要 n+16=30 个元素
        result = compute_adx(high, low, close, n=14)
        assert result == 25.0

    def test_flat_market(self):
        """无趋势市场 — ADX 应接近 0"""
        n_days = 100
        high = np.ones(n_days) * 100 + 0.01 * np.random.randn(n_days)
        low = np.ones(n_days) * 98 + 0.01 * np.random.randn(n_days)
        close = np.ones(n_days) * 99 + 0.01 * np.random.randn(n_days)
        result = compute_adx(high, low, close, n=14)
        assert result >= 0
        assert result <= 100

    def test_strong_trend(self):
        """强趋势市场 — ADX 应较高"""
        n_days = 200
        trend = np.linspace(100, 200, n_days)
        noise = np.random.randn(n_days) * 0.5
        high = trend + noise + 2
        low = trend + noise - 2
        close = trend + noise
        result = compute_adx(high, low, close, n=14)
        # 强趋势下 ADX 通常 > 20
        assert result > 15

    def test_output_range(self):
        """ADX 值应在 [0, 100] 范围内"""
        n_days = 150
        high = 100 + np.cumsum(np.random.randn(n_days))
        low = high - 5 - np.abs(np.random.randn(n_days))
        close = (high + low) / 2 + np.random.randn(n_days)
        result = compute_adx(high, low, close, n=14)
        assert 0 <= result <= 100


class TestComputeSectorRotation:
    """行业轮动速度测试"""

    def test_no_rotation(self):
        """排名完全不变 — 轮动速度应为 0"""
        prev = {"A": 0.10, "B": 0.05, "C": 0.02, "D": -0.01}
        curr = {"A": 0.08, "B": 0.03, "C": 0.01, "D": -0.02}
        # 排名: A>B>C>D 不变
        result = compute_sector_rotation(prev, curr)
        assert result == pytest.approx(0.0, abs=0.01)

    def test_full_rotation(self):
        """排名完全无关（随机轮动）— 轮动速度应接近 1"""
        # 用6个行业，前后期排名完全正交
        prev = {"A": 0.60, "B": 0.50, "C": 0.40, "D": 0.30, "E": 0.20, "F": 0.10}
        curr = {"A": 0.10, "B": 0.60, "C": 0.05, "D": 0.50, "E": 0.03, "F": 0.40}
        # prev rank: A(0)B(1)C(2)D(3)E(4)F(5)
        # curr rank: B(0)D(1)F(2)A(3)C(4)E(5)
        # 这是大幅重新洗牌，ρ 应 < 0.5
        result = compute_sector_rotation(prev, curr)
        assert result > 0.5  # 高轮动 (1-|ρ| > 0.5)

    def test_partial_rotation(self):
        """部分轮动"""
        prev = {"A": 0.10, "B": 0.05, "C": 0.02, "D": -0.01, "E": 0.08}
        curr = {"A": 0.01, "B": 0.08, "C": 0.05, "D": -0.03, "E": 0.10}
        result = compute_sector_rotation(prev, curr)
        assert 0.0 < result < 1.0

    def test_insufficient_sectors(self):
        """行业数不足 — 返回 0"""
        prev = {"A": 0.10, "B": 0.05}
        curr = {"A": -0.02, "B": 0.08}
        result = compute_sector_rotation(prev, curr, min_sectors=4)
        assert result == 0.0

    def test_mismatched_symbols(self):
        """部分 symbol 不重叠 — 仅用公共部分"""
        prev = {"A": 0.10, "B": 0.05, "C": 0.02, "D": -0.01, "X": 0.03}
        curr = {"A": -0.02, "B": 0.08, "C": 0.01, "D": 0.03, "Y": -0.05}
        result = compute_sector_rotation(prev, curr, min_sectors=4)
        assert 0.0 <= result <= 1.0  # 仅用 A/B/C/D


class TestComputeATR:
    """ATR 计算测试"""

    def test_basic_atr(self):
        n_days = 50
        high = 100 + np.cumsum(np.random.randn(n_days) * 0.5)
        low = high - 2 - np.abs(np.random.randn(n_days))
        close = (high + low) / 2 + np.random.randn(n_days) * 0.1
        atr = compute_atr(high, low, close, n=14)
        assert len(atr) == n_days
        assert np.all(np.isnan(atr[:14]))  # 前 n 天为 NaN
        assert np.all(atr[14:] > 0)  # ATR 必须为正


def test_compute_atr_mismatched_lengths():
    """high/low/close 长度不一致时应抛异常"""
    import etf_core
    high = np.random.uniform(10, 20, 100)
    low = np.random.uniform(8, 10, 99)  # 比 high 少 1
    close = np.random.uniform(10, 20, 100)
    try:
        etf_core.compute_atr(high, low, close)
        assert False, "长度不一致应抛异常"
    except Exception as e:
        assert "length" in str(e).lower() or "same" in str(e).lower()


def test_compute_atr_short_array():
    """短于 n+1 的数组应返回全 NaN"""
    import etf_core
    n = 14
    short_len = n  # 等于 n，不足 n+1
    high = np.random.uniform(10, 20, short_len)
    low = np.random.uniform(8, 10, short_len)
    close = np.random.uniform(10, 20, short_len)
    result = etf_core.compute_atr(high, low, close, n)
    assert len(result) == short_len
    assert np.all(np.isnan(result)), f"短数组(长度={short_len})应返回全 NaN"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

--- tests/test_pattern_match.py ---
# -*- coding: utf-8 -*-
"""形态匹配引擎测试 — 含 GPT-5.5 完备性审查要求的 F12-F15 固定样例
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 审查输入: GPT-5.5 via Codex CLI (F12-F15 固定样例规格)"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from core.pattern_match import (
    pattern_match_single,
    compute_pattern_features,
    extract_morph_features,
)


def _generate_random_walk(n_days: int, start_price: float = 100.0) -> np.ndarray:
    """生成随机游走价格序列用于集成测试"""
    np.random.seed(42)
    returns = np.random.randn(n_days) * 0.02
    prices = start_price * np.cumprod(1 + returns)
    return np.asarray(prices, dtype=np.float64)


class TestPatternMatchSingle:
    """pattern_match_single 集成测试"""

    def test_insufficient_data_short_prices(self):
        """价格序列太短"""
        prices = np.array([100.0] * 10)
        result = pattern_match_single(prices, T_idx=5)
        assert result is None

    def test_insufficient_data_small_T_idx(self):
        """T_idx 太小（不足 L_query + M_forward + 10）"""
        prices = _generate_random_walk(100)
        result = pattern_match_single(prices, T_idx=30)
        assert result is None

    def test_basic_extraction(self):
        """基本提取 — 应返回15维非空特征"""
        prices = _generate_random_walk(600)
        T_idx = 500
        result = pattern_match_single(prices, T_idx)
        assert result is not None
        assert len(result) == 15
        # 所有值应为有限数值
        for key, val in result.items():
            assert isinstance(val, (float, int, np.integer)), f"{key} 类型异常: {type(val)}"
            assert np.isfinite(float(val)), f"{key} = {val} 不是有限值"

    def test_no_query_window_leakage(self):
        """前视偏差防护: 所有匹配片段的未来收益端点 < T_idx"""
        prices = _generate_random_walk(800)
        T_idx = 700
        result = pattern_match_single(prices, T_idx)
        assert result is not None
        # 函数内部已保证 fut_end < T_idx，这里验证返回值合理性
        assert -1.0 <= result["avg_future_ret"] <= 1.0

    def test_returns_consistent_shape(self):
        """多次调用应返回一致的特征键集合"""
        prices = _generate_random_walk(600)
        keys = None
        for T_idx in [400, 450, 500]:
            r = pattern_match_single(prices, T_idx)
            if r is None:
                continue
            if keys is None:
                keys = set(r.keys())
            else:
                assert set(r.keys()) == keys

    def test_cos_prefilter_top_effect(self):
        """cos_prefilter_top 参数应影响结果（不同 top 值可能产生不同特征）"""
        prices = _generate_random_walk(600)
        T_idx = 500
        r1 = pattern_match_single(prices, T_idx, cos_prefilter_top=50)
        r2 = pattern_match_single(prices, T_idx, cos_prefilter_top=200)
        # 两者都不应为 None（如果数据足够）
        assert r1 is not None
        assert r2 is not None
        # 注意: 不同 top-k 可能产生不同特征值（因为 sigma_fast 也变了）
        # 这里只验证两者都有效

    def test_deterministic_output(self):
        """相同输入应产生相同输出（无随机性）"""
        prices = _generate_random_walk(600)
        T_idx = 500
        r1 = pattern_match_single(prices, T_idx)
        r2 = pattern_match_single(prices, T_idx)
        assert r1 is not None
        assert r2 is not None
        for key in r1:
            assert r1[key] == pytest.approx(r2[key])


class TestComputePatternFeatures:
    """compute_pattern_features 单元测试 — 固定输入验证"""

    def test_f1_f5_similarity_features(self):
        """F1-F5: 相似度特征 — 固定输入验证"""
        top_scores = np.array([0.9, 0.7, 0.5, 0.3, 0.1])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01, 0.01])
        top_end_indices = np.array([100, 200, 300, 400, 500])
        result = compute_pattern_features(
            top_scores, top_future_rets, top_end_indices, T_back=750,
        )
        assert result["top1_sim"] == 0.9
        assert result["top5_avg_sim"] == pytest.approx(0.5)  # mean of 5
        assert result["sim_decay"] == pytest.approx(0.4)     # 0.9-0.5
        assert result["sim_variance"] > 0                    # 应有方差
        assert result["match_distance_ratio"] == pytest.approx(0.4 / 0.9)

    def test_f6_f11_future_ret_features(self):
        """F6-F11: 后续表现特征"""
        top_scores = np.array([0.9, 0.7, 0.5])
        top_future_rets = np.array([0.06, -0.03, 0.02])
        top_end_indices = np.array([100, 200, 300])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)

        assert result["avg_future_ret"] == pytest.approx(np.mean([0.06, -0.03, 0.02]))
        # weighted: (0.9*0.06 + 0.7*(-0.03) + 0.5*0.02) / (0.9+0.7+0.5) = (0.054-0.021+0.01)/2.1
        assert result["weighted_future_ret"] == pytest.approx(0.043 / 2.1)
        assert result["median_future_ret"] == 0.02
        assert result["ret_sign_consistency"] == pytest.approx(2 / 3)  # 2 positive
        assert result["best_match_ret"] == 0.06
        assert result["max_dd_in_matches"] == 0.03  # max(0, -(-0.03)) = 0.03

    # ═══════════════════════════════════════════════════════════════
    # v2: GPT-5.5 完备性审查 P0 — F12-F15 固定样例
    # ═══════════════════════════════════════════════════════════════

    def test_f12_time_span(self):
        """F12: 匹配时间跨度 — max_index - min_index"""
        top_scores = np.array([0.9, 0.7, 0.5, 0.4])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01])
        top_end_indices = np.array([100, 120, 160, 220])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        assert result["match_time_span"] == 120.0  # 220 - 100
        assert result["match_time_span_ratio"] == pytest.approx(120 / 750)

    def test_f13_time_span_ratio(self):
        """F13: 时间跨度比率 — (max-min)/T_back"""
        top_scores = np.array([0.9, 0.7])
        top_future_rets = np.array([0.05, -0.02])
        # span=500, T_back=1000 → ratio=0.5
        top_end_indices = np.array([100, 600])
        result = compute_pattern_features(
            top_scores, top_future_rets, top_end_indices, T_back=1000,
        )
        assert result["match_time_span_ratio"] == 0.5

    def test_f14_cluster_ratio(self):
        """F14: 聚类比率 — 60日窗口内最大匹配数/K"""
        top_scores = np.array([0.81, 0.80, 0.79, 0.90])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01])
        # indices sorted: [100, 120, 160, 220]
        # searchsorted(x+60, side="right") 行为:
        #   i=0: searchsorted(160, right) → 3 (160插入到现有160之后) → 3-0=3
        #   i=1: searchsorted(180, right) → 2 → 2-1=1
        #   i=2: searchsorted(220, right) → 4 (220插入到现有220之后) → 4-2=2
        #   i=3: searchsorted(280, right) → 4 → 4-3=1
        # max_in_window = 3, ratio = 3/4 = 0.75
        top_end_indices = np.array([100, 120, 160, 220])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        assert result["match_cluster_ratio"] == pytest.approx(3 / 4)  # 3/4=0.75

    def test_f15_n_matches_above_thresh(self):
        """F15: 高于0.8阈值的匹配数 — 严格 > 0.8"""
        top_scores = np.array([0.81, 0.80, 0.79, 0.90])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01])
        top_end_indices = np.array([100, 200, 300, 400])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        # 0.81>0.8 ✓, 0.80>0.8 ✗ (不严格大于), 0.79 ✗, 0.90 ✓
        assert result["n_matches_above_thresh"] == 2

    def test_f15_boundary_exactly_08(self):
        """F15: 恰好等于0.8不计入（> 0.8，非 >= 0.8）"""
        top_scores = np.array([0.80, 0.80])
        top_future_rets = np.array([0.05, -0.02])
        top_end_indices = np.array([100, 200])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        assert result["n_matches_above_thresh"] == 0


class TestExtractMorphFeatures:
    """extract_morph_features 便捷接口测试"""

    def test_alias(self):
        """extract_morph_features 应与 pattern_match_single 结果一致"""
        prices = _generate_random_walk(600)
        T_idx = 500
        r1 = pattern_match_single(prices, T_idx)
        r2 = extract_morph_features(prices, T_idx)
        assert (r1 is None) == (r2 is None)
        if r1 is not None:
            for key in r1:
                assert r1[key] == pytest.approx(r2[key])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Host '"'--- project Python files ---'; Get-ChildItem -LiteralPath 'src' -Recurse -File | Select-Object FullName; Write-Host '--- selected native-facing tests ---'; Select-String -LiteralPath 'tests/test_dtw.py','tests/test_technical.py','tests/test_pattern_match.py','verify_etf_core.py','verify_batch.py' -Pattern '"'^'"\\s*def test_|etf_core\\.|expected|known|boundary|tie|NaN|Inf|nan|inf' -Encoding UTF8 | ForEach-Object { '{0}:{1}: {2}' -f "'$_.Path,$_.LineNumber,$_.Line.Trim() }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 203ms:
--- project Python files ---

--- selected native-facing tests ---
FullName                                                                                     
--------                                                                                     
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\dtw.py                                     
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\market_features.py                         
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\metrics.py                                 
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\pattern_match.py                           
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\risk_controls.py                           
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\technical.py                               
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__init__.py                                
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\dtw.cpython-312.pyc            
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\dtw.cpython-314.pyc            
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\market_features.cpython-312.pyc
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\metrics.cpython-312.pyc        
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\pattern_match.cpython-312.pyc  
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\pattern_match.cpython-314.pyc  
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\risk_controls.cpython-312.pyc  
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\technical.cpython-312.pyc      
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\__init__.cpython-312.pyc       
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\__init__.cpython-314.pyc       
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\CMakeLists.txt                              
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\etf_core.cpp                                
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\__init__.py                                 
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\pyi\etf_core.pyi                            
E:\workspace\projects\形态匹配ETF策略-pybind11\src\strategy\__init__.py                            
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:3: > 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:4: > v2 新增: NaN 边界测试 + cosine 阈值测试 (GPT-5.5 完备性审查 P1)"""
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:27: def test_normal_case(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:35: def test_constant_prices(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:42: def test_short_series(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:47: def test_zero_price_handling(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:51: assert not np.any(np.isnan(result))
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:52: assert not np.any(np.isinf(result))
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:54: def test_nan_in_prices(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:55: """含 NaN 的价格 — NaN 收益率应被过滤"""
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:56: # log(0) = -inf → diff 可能产生 nan
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:59: # 对恒定价格返回全零，不会有 NaN
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:62: assert not np.any(np.isnan(result))
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:64: # v2 新增: 真实 NaN 边界测试 (GPT-5.5 完备性审查 P1)
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:66: # 任一价格为 NaN/Inf 即返回空数组，因此以下测试改为验证新契约。
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:67: def test_nan_value_in_array(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:68: """数组中含 np.nan — 窗口级检查应返回空数组"""
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:69: result = standardize_returns(np.array([100.0, np.nan, 101.0]))
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:72: def test_all_nan(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:73: """全 NaN — 窗口级检查应返回空数组"""
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:74: result = standardize_returns(np.array([np.nan, np.nan]))
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:77: def test_zero_then_valid(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:78: """价格为0后被clip — 验证clip不产生NaN"""
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:81: assert not np.any(np.isnan(result))
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:87: def test_identical_vectors(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:91: def test_opposite_vectors(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:95: def test_orthogonal_vectors(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:100: def test_zero_vector(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:106: def test_near_zero_norm(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:113: def test_exactly_at_threshold(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:125: def test_identical_sequences(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:131: def test_same_length_sequences(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:137: assert not np.isnan(d)
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:138: assert not np.isinf(d)
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:140: def test_different_length_sequences(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:146: assert not np.isnan(d)
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:147: assert not np.isinf(d)
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:149: def test_window_constraint(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:158: def test_empty_input(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:159: """空序列应返回 inf"""
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:160: assert dtw_distance(np.array([]), np.array([1.0, 2.0])) == np.inf
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:161: assert dtw_distance(np.array([1.0, 2.0]), np.array([])) == np.inf
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:163: def test_single_element(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:172: def test_basic_batch(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:179: def test_top_k(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:188: def test_consistency_with_single(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:196: def test_empty_candidates(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:200: def test_mismatched_lengths(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:211: def test_basic_generation(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py:221: def test_insufficient_data(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:3: > 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03"""
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:19: def test_insufficient_data(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:28: def test_flat_market(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:38: def test_strong_trend(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:50: def test_output_range(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:63: def test_no_rotation(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:71: def test_full_rotation(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:82: def test_partial_rotation(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:89: def test_insufficient_sectors(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:96: def test_mismatched_symbols(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:107: def test_basic_atr(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:114: assert np.all(np.isnan(atr[:14]))  # 前 n 天为 NaN
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:118: def test_compute_atr_mismatched_lengths():
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:125: etf_core.compute_atr(high, low, close)
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:131: def test_compute_atr_short_array():
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:132: """短于 n+1 的数组应返回全 NaN"""
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:139: result = etf_core.compute_atr(high, low, close, n)
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py:141: assert np.all(np.isnan(result)), f"短数组(长度={short_len})应返回全 NaN"
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:3: > 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:31: def test_insufficient_data_short_prices(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:37: def test_insufficient_data_small_T_idx(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:43: def test_basic_extraction(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:55: def test_no_query_window_leakage(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:64: def test_returns_consistent_shape(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:77: def test_cos_prefilter_top_effect(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:89: def test_deterministic_output(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:104: def test_f1_f5_similarity_features(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:118: def test_f6_f11_future_ret_features(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:137: def test_f12_time_span(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:146: def test_f13_time_span_ratio(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:157: def test_f14_cluster_ratio(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:172: def test_f15_n_matches_above_thresh(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:181: def test_f15_boundary_exactly_08(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py:193: def test_alias(self):
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:5: > 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:10: python verify_etf_core.py          # 完整验证
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:11: python verify_etf_core.py --quick  # 快速冒烟测试
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:55: if np.allclose(py_arr, cpp_arr, atol=tol, rtol=1e-12, equal_nan=True):
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:67: if np.isnan(py_val) and np.isnan(cpp_val):
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:68: print(f"  ✅ {name}: both NaN")
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:124: cpp_r = np.array(etf_core.standardize_returns(prices))
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:132: cpp_r = np.array(etf_core.standardize_returns(prices))
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:155: cpp_v = etf_core.cosine_similarity(x, y)
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:173: cpp_d = etf_core.dtw_distance(x, y, 5)
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:190: cpp_v = etf_core.compute_adx(high, low, close, 14)
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:209: cpp_r = etf_core.pattern_match_single(prices, T_idx)
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:247: etf_core.dtw_distance(x, y, 5)
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_etf_core.py:266: etf_core.pattern_match_single(prices, T_idx)
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:4: > 模型 provenance: Kimi-K2.7-Code (via Kimi Code CLI), 2026-07-03
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:51: for i, key in enumerate(etf_core.FEATURE_KEYS):
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:55: if np.isnan(a) and np.isnan(b):
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:70: single_res = etf_core.pattern_match_single(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:81: features, mask = etf_core.pattern_match_batch(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:103: boundary_Ts = np.array([0, 5, min_T - 1, min_T], dtype=np.int64)
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:104: features, mask = etf_core.pattern_match_batch(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:106: boundary_Ts,
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:115: for i, T_idx in enumerate(boundary_Ts):
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:124: _, single_mask = etf_core.pattern_match_batch(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:151: _ = etf_core.pattern_match_single(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:155: _ = etf_core.pattern_match_batch(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:165: etf_core.pattern_match_single(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:183: features, mask = etf_core.pattern_match_batch(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:197: speedup = t_single / t_batch if t_batch > 0 else float("inf")
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:208: features, mask = etf_core.pattern_match_batch(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:218: features, mask = etf_core.pattern_match_batch(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:228: features, mask = etf_core.pattern_match_batch(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:235: single_res = etf_core.pattern_match_single(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:238: for i, key in enumerate(etf_core.FEATURE_KEYS):
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:245: etf_core.pattern_match_single(
E:\workspace\projects\形态匹配ETF策略-pybind11\verify_batch.py:253: etf_core.pattern_match_batch(



Inspected the production target and all eight exported C++ functions. The current `etf_core` target is a pybind11 `MODULE_LIBRARY`, so the test CMake file needs a linkable test-only static form of the same production source while preserving direct C++ calls and avoiding Python module import/dispatch.
  ✓ Inspect project instructions, CMake structure, headers, and src/cpp/etf_core.cpp
  ✓ Design comprehensive doctest cases for all eight core functions
  → Create tests/test_etf_core.cpp and tests/CMakeLists.txt without modifying existing files
  • Review new files statically for API/style/CMake correctness (do not run tests)
mcp: node_repl/js started
mcp: node_repl/js (failed)
tool call error: tool call failed for `node_repl/js`

Caused by:
    Mcp error: -32602: js: codex/sandbox-state-meta: missing field `sandboxPolicy`
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; foreach ($f in @('"'C:\\Users\\33455\\_apply_etf_tests.py','C:\\Users\\33455\\_apply_etf_patch.py','C:\\Users\\33455\\_fix_etf_patch.py')) { if (Test-Path -LiteralPath "'$f) { Write-Host "--- $f ---"; Get-Content -LiteralPath $f -Raw -Encoding UTF8 } }' in C:\Users\33455
 succeeded in 188ms:
--- C:\Users\33455\_apply_etf_tests.py ---
from pathlib import Path

ROOT = Path(r"C:\Users\33455\_review_etf_pattern")


def read(rel: str) -> str:
    with open(ROOT / rel, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(content)


test_content = '''from __future__ import annotations

import importlib.machinery
import os
from pathlib import Path
import sys

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import etf_core
from core.dtw import cosine_similarity as py_cosine_similarity
from core.dtw import dtw_distance as py_dtw_distance
from core.dtw import standardize_returns as py_standardize_returns
from core.pattern_match import pattern_match_single as py_pattern_match_single
from core.technical import compute_adx as py_compute_adx
from core.technical import compute_atr as py_compute_atr


FEATURE_KEYS = (
    "top1_sim",
    "top5_avg_sim",
    "sim_decay",
    "sim_variance",
    "match_distance_ratio",
    "avg_future_ret",
    "weighted_future_ret",
    "median_future_ret",
    "ret_sign_consistency",
    "best_match_ret",
    "max_dd_in_matches",
    "match_time_span",
    "match_time_span_ratio",
    "match_cluster_ratio",
    "n_matches_above_thresh",
)


@pytest.fixture(scope="module")
def prices() -> np.ndarray:
    rng = np.random.default_rng(42)
    returns = rng.normal(0.0005, 0.01, size=800)
    return np.ascontiguousarray(
        100.0 * np.exp(np.cumsum(returns)),
        dtype=np.float64,
    )


def assert_feature_dicts_close(
    actual: dict[str, float] | None,
    expected: dict[str, float] | None,
) -> None:
    assert actual is not None
    assert expected is not None
    assert tuple(actual) == FEATURE_KEYS
    assert tuple(expected) == FEATURE_KEYS
    for key in FEATURE_KEYS:
        assert actual[key] == pytest.approx(expected[key], abs=1e-6, rel=1e-9)


def test_binary_extension_and_installed_stub() -> None:
    module_path = Path(etf_core.__file__).resolve()
    assert any(
        str(module_path).endswith(suffix)
        for suffix in importlib.machinery.EXTENSION_SUFFIXES
    )
    assert tuple(etf_core.FEATURE_KEYS) == FEATURE_KEYS

    if os.environ.get("ETF_EXPECT_INSTALLED_WHEEL") == "1":
        assert module_path.with_name("etf_core.pyi").is_file()


def test_dtw_kernels_match_python_reference() -> None:
    price_window = np.array([100.0, 101.0, 99.5, 102.0, 103.0, 101.5])
    cpp_returns = etf_core.standardize_returns(price_window)
    py_returns = py_standardize_returns(price_window)

    assert cpp_returns.dtype == np.float64
    assert cpp_returns.shape == (len(price_window) - 1,)
    np.testing.assert_allclose(cpp_returns, py_returns, atol=1e-12, rtol=1e-12)

    other = np.array([0.2, -0.1, 0.4, 0.0, -0.3], dtype=np.float64)
    assert etf_core.cosine_similarity(cpp_returns, other) == pytest.approx(
        py_cosine_similarity(py_returns, other),
        abs=1e-12,
    )
    assert etf_core.dtw_distance(cpp_returns, other, window=2) == pytest.approx(
        py_dtw_distance(py_returns, other, window=2),
        abs=1e-12,
    )


def test_dtw_batch_contract_and_top_k() -> None:
    query = np.array([0.1, -0.2, 0.3, 0.0], dtype=np.float64)
    candidates = np.array(
        [
            [0.1, -0.2, 0.3, 0.0],
            [0.2, -0.1, 0.25, 0.05],
            [-0.3, 0.2, -0.1, 0.4],
        ],
        dtype=np.float64,
    )
    expected = np.array(
        [py_dtw_distance(query, row, window=2) for row in candidates],
        dtype=np.float64,
    )

    distances = etf_core.dtw_distance_batch(query, candidates, window=2)
    assert isinstance(distances, np.ndarray)
    assert distances.shape == (3,)
    assert distances.dtype == np.float64
    np.testing.assert_allclose(distances, expected, atol=1e-12, rtol=1e-12)

    indices, top_distances = etf_core.dtw_distance_batch(
        query,
        candidates,
        window=2,
        top_k=2,
    )
    expected_indices = np.argsort(expected)[:2]
    assert indices.dtype == np.int64
    np.testing.assert_array_equal(indices, expected_indices)
    np.testing.assert_allclose(
        top_distances,
        expected[expected_indices],
        atol=1e-12,
        rtol=1e-12,
    )


def test_technical_indicators_match_python_reference(prices: np.ndarray) -> None:
    rng = np.random.default_rng(7)
    high = prices[:160] + rng.uniform(0.1, 1.0, size=160)
    low = prices[:160] - rng.uniform(0.1, 1.0, size=160)
    close = prices[:160].copy()

    assert etf_core.compute_adx(high, low, close, 14) == pytest.approx(
        py_compute_adx(high, low, close, 14),
        abs=1e-10,
    )

    cpp_atr = etf_core.compute_atr(high, low, close, 14)
    py_atr = py_compute_atr(high, low, close, 14)
    assert cpp_atr.dtype == np.float64
    assert cpp_atr.shape == close.shape
    np.testing.assert_allclose(
        cpp_atr,
        py_atr,
        atol=1e-10,
        rtol=1e-12,
        equal_nan=True,
    )


def test_pattern_match_single_parity_and_invalid_history(
    prices: np.ndarray,
) -> None:
    cpp_result = etf_core.pattern_match_single(prices, T_idx=500)
    py_result = py_pattern_match_single(prices, T_idx=500)
    assert_feature_dicts_close(cpp_result, py_result)

    assert etf_core.pattern_match_single(prices, T_idx=5) is None
    with pytest.raises(ValueError, match="match_step"):
        etf_core.pattern_match_single(prices, T_idx=500, match_step=0)


def test_pattern_match_batch_shape_mask_and_single_parity(
    prices: np.ndarray,
) -> None:
    t_indices = np.array([5, 500, 600], dtype=np.int64)
    features, valid_mask = etf_core.pattern_match_batch(prices, t_indices)

    assert features.dtype == np.float64
    assert features.shape == (2, len(FEATURE_KEYS))
    assert valid_mask.dtype == np.bool_
    np.testing.assert_array_equal(valid_mask, [False, True, True])

    valid_t_indices = t_indices[valid_mask]
    for row, t_idx in zip(features, valid_t_indices, strict=True):
        single_result = etf_core.pattern_match_single(prices, int(t_idx))
        assert single_result is not None
        expected_row = np.array(
            [single_result[key] for key in FEATURE_KEYS],
            dtype=np.float64,
        )
        np.testing.assert_allclose(row, expected_row, atol=1e-6, rtol=1e-9)


def test_invalid_array_lengths_raise() -> None:
    high = np.ones(20, dtype=np.float64)
    low = np.ones(19, dtype=np.float64)
    close = np.ones(20, dtype=np.float64)
    with pytest.raises(ValueError):
        etf_core.compute_atr(high, low, close)
'''
write("tests/test_etf_core_extension.py", test_content)

example_content = '''from __future__ import annotations

import numpy as np

import etf_core


def main() -> None:
    rng = np.random.default_rng(42)
    returns = rng.normal(0.0005, 0.01, size=1000)
    prices = np.ascontiguousarray(
        100.0 * np.exp(np.cumsum(returns)),
        dtype=np.float64,
    )

    features = etf_core.pattern_match_single(prices, T_idx=800)
    if features is None:
        raise RuntimeError("Not enough valid history for pattern matching")

    for key in etf_core.FEATURE_KEYS:
        print(f"{key}: {features[key]:.6f}")


if __name__ == "__main__":
    main()
'''
write("examples/minimal_example.py", example_content)

ci = read(".github/workflows/ci.yml")
ci = ci.replace(
    "        env:\r\n"
    "          PYTHONIOENCODING: utf-8\r\n"
    "        run: python -m pytest tests/ -v\r\n",
    "        env:\r\n"
    "          PYTHONIOENCODING: utf-8\r\n"
    '          ETF_EXPECT_INSTALLED_WHEEL: "1"\r\n'
    "        run: python -m pytest tests/ -v\r\n",
    1,
)
write(".github/workflows/ci.yml", ci)

readme = read("README.md")
readme = readme.replace(
    "[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)",
    "[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)",
)
readme = readme.replace(
    "```bash\r\n"
    "pip install git+https://github.com/redamancy231-create/etf-pattern-match-pybind11.git\r\n"
    "```\r\n"
    "\r\n"
    "### 从源码构建 (cmake)",
    "```bash\r\n"
    "pip install git+https://github.com/redamancy231-create/etf-pattern-match-pybind11.git\r\n"
    "python examples/minimal_example.py\r\n"
    "```\r\n"
    "\r\n"
    "最小可运行示例见 [`examples/minimal_example.py`](examples/minimal_example.py)。\r\n"
    "See [`examples/minimal_example.py`](examples/minimal_example.py) for a minimal runnable example.\r\n"
    "\r\n"
    "### 从源码构建 (cmake)",
)
readme = readme.replace(
    "├── tests/                      # 54 unit tests\r\n"
    "├── notebooks/",
    "├── tests/                      # Python behavior + compiled-extension parity tests\r\n"
    "├── examples/\r\n"
    "│   └── minimal_example.py      # Minimal installed-package usage\r\n"
    "├── notebooks/",
)
readme = readme.replace(
    "- 54 unit tests + 2 verification scripts",
    "- Python unit tests + mandatory compiled-extension parity tests + 2 verification scripts",
)
readme = readme.replace(
    "- 54 项单元测试 + 2 个验证脚本",
    "- Python 单元测试 + 强制 C++ 扩展一致性测试 + 2 个验证脚本",
)
readme = readme.replace(
    "- Python 3.12.7 + NumPy",
    "- Python 3.10+ + NumPy",
)
write("README.md", readme)

print("Added extension tests, minimal example, and README updates.")
--- C:\Users\33455\_apply_etf_patch.py ---
from pathlib import Path

ROOT = Path(r"C:\Users\33455\_review_etf_pattern")


def read(rel: str) -> str:
    with open(ROOT / rel, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(content)


cmake = read("CMakeLists.txt")
cmake = cmake.replace(
    "find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Module)",
    "find_package(Python 3.10 REQUIRED COMPONENTS Interpreter Development.Module)",
)
cmake = cmake.replace(
    "set(CMAKE_CXX_EXTENSIONS OFF)\r\n",
    "set(CMAKE_CXX_EXTENSIONS OFF)\r\n"
    "\r\n"
    "option(ETF_ENABLE_SANITIZERS\r\n"
    "    \"Enable AddressSanitizer and UndefinedBehaviorSanitizer\" OFF\r\n"
    ")\r\n",
)
cmake = cmake.replace(
    "# Install — scikit-build-core 需要这些指令来打包 wheel\r\n"
    "install(TARGETS etf_core DESTINATION src/cpp)\r\n"
    "# Also expose the extension at the top level for ``import etf_core`` after pip install.\r\n"
    "install(TARGETS etf_core DESTINATION .)\r\n"
    "# Match scikit-build-core's wheel package destination (``cpp``) as well.\r\n"
    "install(TARGETS etf_core DESTINATION cpp)\r\n",
    "# Install — wheel 只包含顶层扩展与同名类型存根。\r\n"
    "install(TARGETS etf_core\r\n"
    "    LIBRARY DESTINATION .\r\n"
    "    RUNTIME DESTINATION .\r\n"
    ")\r\n"
    "install(FILES src/cpp/pyi/etf_core.pyi DESTINATION .)\r\n",
)
write("CMakeLists.txt", cmake)

cpp_cmake = read("src/cpp/CMakeLists.txt")
cpp_cmake = cpp_cmake.replace(
    'message(STATUS "C++ module: etf_core")\r\n',
    "if(MSVC)\r\n"
    "    target_compile_options(etf_core PRIVATE /W4)\r\n"
    "else()\r\n"
    "    target_compile_options(etf_core PRIVATE -Wall -Wextra -Wpedantic)\r\n"
    "endif()\r\n"
    "\r\n"
    "if(ETF_ENABLE_SANITIZERS)\r\n"
    '    if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")\r\n'
    "        target_compile_options(\r\n"
    "            etf_core PRIVATE\r\n"
    "            -fsanitize=address,undefined\r\n"
    "            -fno-omit-frame-pointer\r\n"
    "        )\r\n"
    "        target_link_options(\r\n"
    "            etf_core PRIVATE\r\n"
    "            -fsanitize=address,undefined\r\n"
    "        )\r\n"
    "    else()\r\n"
    "        message(FATAL_ERROR\r\n"
    '            "ETF_ENABLE_SANITIZERS requires GCC or Clang")\r\n'
    "    endif()\r\n"
    "endif()\r\n"
    "\r\n"
    'message(STATUS "C++ module: etf_core")\r\n',
)
write("src/cpp/CMakeLists.txt", cpp_cmake)

pyproject = read("pyproject.toml").replace(
    'wheel.packages = ["src/cpp"]',
    "wheel.packages = []",
)
write("pyproject.toml", pyproject)

ci = """name: CI

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  wheel-test:
    name: ${{ matrix.os }} / Python ${{ matrix.python-version }}
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ["3.10", "3.12"]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install build and test dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install build numpy pytest

      - name: Build wheel
        run: python -m build --wheel

      - name: Install built wheel
        run: >-
          python -c "import glob, subprocess, sys;
          wheels = glob.glob('dist/*.whl');
          assert len(wheels) == 1, wheels;
          subprocess.check_call([sys.executable, '-m', 'pip', 'install', wheels[0]])"

      - name: Run Python and compiled-extension tests
        env:
          PYTHONIOENCODING: utf-8
        run: python -m pytest tests/ -v

      - name: Run minimal example
        env:
          PYTHONIOENCODING: utf-8
        run: python examples/minimal_example.py

      - name: Upload wheel artifact
        uses: actions/upload-artifact@v4
        with:
          name: wheel-${{ runner.os }}-py${{ matrix.python-version }}
          path: dist/*.whl
          if-no-files-found: error

  sanitizers:
    name: Linux ASan/UBSan
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install cmake numpy pybind11 pytest

      - name: Configure sanitizer build
        run: >-
          cmake -S . -B build
          -DCMAKE_BUILD_TYPE=RelWithDebInfo
          -DPython_EXECUTABLE=$(which python)
          -DETF_ENABLE_SANITIZERS=ON

      - name: Build sanitizer extension
        run: cmake --build build --config RelWithDebInfo --parallel

      - name: Run compiled-extension tests under sanitizers
        run: |
          export LD_PRELOAD=$(gcc -print-file-name=libasan.so)
          export ASAN_OPTIONS=detect_leaks=0:halt_on_error=1
          export UBSAN_OPTIONS=print_stacktrace=1:halt_on_error=1
          export PYTHONPATH=$PWD/build
          python -m pytest tests/test_etf_core_extension.py -v
"""
write(".github/workflows/ci.yml", ci)

verify = read("verify_etf_core.py")
verify = verify.replace(
    "import argparse\r\nimport numpy as np\r\n\r\n"
    'sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))\r\n',
    "import argparse\r\nfrom pathlib import Path\r\n\r\n"
    "import numpy as np\r\n\r\n"
    "ROOT = Path(__file__).resolve().parent\r\n"
    'sys.path.insert(0, str(ROOT / "src"))\r\n',
)
verify = verify.replace(
    '    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "build", "Release"))\r\n'
    "    import etf_core\r\n",
    '    for build_path in (ROOT / "build" / "Release", ROOT / "build"):\r\n'
    "        if build_path.is_dir():\r\n"
    "            sys.path.insert(0, str(build_path))\r\n"
    "    import etf_core\r\n",
)
write("verify_etf_core.py", verify)

batch = read("verify_batch.py")
batch = batch.replace(
    "import os\r\nimport numpy as np\r\n\r\n"
    'sys.path.insert(0, os.path.join(os.path.dirname(__file__), "build", "Release"))\r\n'
    "import etf_core\r\n",
    "from pathlib import Path\r\n\r\n"
    "import numpy as np\r\n\r\n"
    "ROOT = Path(__file__).resolve().parent\r\n"
    'for build_path in (ROOT / "build" / "Release", ROOT / "build"):\r\n'
    "    if build_path.is_dir():\r\n"
    "        sys.path.insert(0, str(build_path))\r\n"
    "import etf_core\r\n",
)
write("verify_batch.py", batch)

print("Patched build, CI, packaging, and verification scripts.")
--- C:\Users\33455\_fix_etf_patch.py ---
from pathlib import Path

root = Path(r"C:\Users\33455\_review_etf_pattern")


def read(rel: str) -> str:
    with open(root / rel, "r", encoding="utf-8", newline="") as handle:
        return handle.read()


def write_crlf(rel: str, content: str) -> None:
    normalized = content.replace("\r\n", "\n").replace("\n", "\r\n")
    with open(root / rel, "w", encoding="utf-8", newline="") as handle:
        handle.write(normalized)


ci = read(".github/workflows/ci.yml")
ci = ci.replace(
    "        env:\n"
    "          PYTHONIOENCODING: utf-8\n"
    "        run: python -m pytest tests/ -v\n",
    "        env:\n"
    "          PYTHONIOENCODING: utf-8\n"
    '          ETF_EXPECT_INSTALLED_WHEEL: "1"\n'
    "        run: python -m pytest tests/ -v\n",
    1,
)
write_crlf(".github/workflows/ci.yml", ci)
write_crlf("tests/test_etf_core_extension.py", read("tests/test_etf_core_extension.py"))
write_crlf("examples/minimal_example.py", read("examples/minimal_example.py"))

readme = read("README.md").replace(
    "pip install git+https://github.com/redamancy231-create/etf-pattern-match-pybind11.git\r\n"
    "python examples/minimal_example.py\r\n",
    "pip install git+https://github.com/redamancy231-create/etf-pattern-match-pybind11.git\r\n",
)
with open(root / "README.md", "w", encoding="utf-8", newline="") as handle:
    handle.write(readme)

print("Fixed CI environment, line endings, and Quick Start command.")

warning: Skill descriptions were shortened to fit the 2% skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
context compacted
warning: Heads up: Long threads and multiple compactions can cause the model to be less accurate. Start a new thread when possible to keep threads small and targeted.
  → 检查现有 C++ 源码与 CMake 结构，确认函数签名和行为
  • 编写 tests/test_etf_core.cpp，覆盖 8 个核心函数
  • 编写 tests/CMakeLists.txt，配置 doctest 与原生测试目标
  • 静态复核编码、文件内容与 Git 变更（不编译、不运行测试）
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Get-ChildItem -Force; Write-Output '"'--- src/cpp/etf_core.cpp ---'; Get-Content -Raw -Encoding UTF8 'src/cpp/etf_core.cpp'; Write-Output '--- src/cpp/CMakeLists.txt ---'; Get-Content -Raw -Encoding UTF8 'src/cpp/CMakeLists.txt'; Write-Output '--- root CMakeLists.txt ---'; Get-Content -Raw -Encoding UTF8 'CMakeLists.txt'" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 241ms:


    目录: E:\workspace\projects\形态匹配ETF策略-pybind11


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d--h--         2026/7/17     17:34                .git                                                                 
d-----          2026/7/5     12:58                .github                                                              
d-----          2026/7/3     21:42                .pytest_cache                                                        
d-----         2026/7/16     17:17                benchmarks                                                           
d-----         2026/7/12     18:00                build                                                                
d-----         2026/7/12     19:56                docs                                                                 
d-----         2026/7/12     19:41                notebooks                                                            
d-----          2026/7/3     21:29                src                                                                  
d-----         2026/7/12     19:41                tests                                                                
d-----         2026/7/17     17:32                _review                                                              
d-----         2026/7/12     19:33                审查提示词                                                                
-a----          2026/7/4     14:22            397 .gitignore                                                           
-a----         2026/7/16     16:48           1434 CHANGELOG.md                                                         
-a----         2026/7/16     17:29            853 CITATION.cff                                                         
-a----         2026/7/12     19:55          12069 CLAUDE.md                                                            
-a----         2026/7/16     16:48           2653 CMakeLists.txt                                                       
-a----         2026/7/16     17:30           1881 CONTRIBUTING.md                                                      
-a----         2026/7/16     16:18           4484 improvement_plan.md                                                  
-a----          2026/7/4     14:03           1069 LICENSE                                                              
-a----         2026/7/16     17:02           6144 project_status.md                                                    
-a----         2026/7/16     16:32           3641 prompt_p0_build.md                                                   
-a----         2026/7/16     16:52           5077 prompt_p1_benchmark.md                                               
-a----         2026/7/16     16:48            867 pyproject.toml                                                       
-a----         2026/7/16     17:28          14342 README.md                                                            
-a----         2026/7/16     16:48            405 SECURITY.md                                                          
-a----         2026/7/12     19:58          62758 social-preview.png                                                   
-a----          2026/7/4     13:16           8665 verify_batch.py                                                      
-a----          2026/7/4     14:19           9507 verify_etf_core.py                                                   
--- src/cpp/etf_core.cpp ---
/**
 * etf_core.cpp — 形态匹配ETF策略 C++ 加速模块 (pybind11)
 * =============================================================
 *
 * > 模型 provenance:
 * >   DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03:
 * >     standardize_returns, cosine_similarity, dtw_distance,
 * >     compute_adx, compute_atr, pattern_match_single, 模块骨架, PYBIND11_MODULE
 * >   Kimi-K2.7-Code (via Kimi Code CLI), 2026-07-03:
 * >     pattern_match_batch, cosine_similarity_vec, dtw_distance_vec,
 * >     compute_pattern_features_cpp, 预计算缓存架构, v3 修订
 * >   DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-12:
 * >     dtw_distance_batch, 模块绑定
 *
 * 来源: 形态匹配ETF组合策略_V3.3.py
 *   - dtw_distance:         行 339-359
 *   - standardize_returns:  行 362-373
 *   - cosine_similarity:    行 376-382
 *   - _compute_adx_from_df: 行 757-795
 *   - pattern_match_single: 行 389-627 (含 V3.0 余弦预筛选)
 *   - pattern_match_batch:  新增 — 同 ETF 多 T_idx 批量形态匹配
 *
 * 工具链: MSVC 19.51 + pybind11 3.0.4 + C++20
 * 编译:   cmake -B build -DPython_EXECUTABLE=... && cmake --build build --config Release
 *
 * 审查: Kimi-K2.7-Code (魔鬼代言人) + GPT-5.5 via Codex CLI (完备性)
 *
 * v2 修订 (基于双审):
 *   - 三模块合并为一个 etf_core
 *   - GIL释放边界明确标注
 *   - py::ssize_t 索引 (MSVC兼容)
 *   - forcecast 策略处理 dtype
 *   - 浮点容差分两层 (距离 <1e-8, 得分 <1e-6)
 *   - 返回结构契约: dict key 稳定, None 语义一致
 *
 * v3 修订:
 *   - 新增 pattern_match_batch，消除同 ETF 多 T_idx 场景下的 Python 往返和重复标准化
 */

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <limits>
#include <numeric>
#include <optional>
#include <stdexcept>

namespace py = pybind11;

// ── 类型别名 (v2: forcecast 策略) ──
using ArrD  = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;

// ═══════════════════════════════════════════════════════════════
// 第一部分: 序列标准化 (V3.3.py 行 362-373)
// ═══════════════════════════════════════════════════════════════

std::vector<double> standardize_returns_cpp(const double* prices, py::ssize_t n) {
    if (n < 2) {
        return {};  // 返回空向量表示无效窗口
    }

    // 窗口级检查：任一价格为非有限值 → 整个窗口无效
    for (py::ssize_t i = 0; i < n; ++i) {
        if (!std::isfinite(prices[i])) {
            return {};
        }
    }

    // 计算对数收益率（所有价格已通过有限性检查，长度固定为 n-1）
    std::vector<double> rets;
    rets.reserve(n - 1);
    for (py::ssize_t i = 1; i < n; ++i) {
        double p_prev = std::max(prices[i - 1], 1e-12);
        double p_curr = std::max(prices[i], 1e-12);
        rets.push_back(std::log(p_curr / p_prev));
    }

    if (rets.empty()) {
        return {};
    }

    // 去均值
    double mean = std::accumulate(rets.begin(), rets.end(), 0.0) / rets.size();
    for (auto& r : rets) r -= mean;

    // 标准差
    double sq_sum = 0.0;
    for (auto r : rets) sq_sum += r * r;
    double std_val = std::sqrt(sq_sum / rets.size());

    if (std_val < 1e-12) {
        return rets;  // 已去均值，不再除以 std
    }

    for (auto& r : rets) r /= std_val;
    return rets;
}

// Python 绑定包装
ArrD standardize_returns(ArrD price_series) {
    auto buf = price_series.unchecked<1>();
    py::ssize_t n = buf.shape(0);
    const double* ptr = buf.data(0);

    std::vector<double> result_vec;
    {
        py::gil_scoped_release release;
        result_vec = standardize_returns_cpp(ptr, n);
    }

    py::ssize_t m = static_cast<py::ssize_t>(result_vec.size());
    ArrD result(m);
    auto res_buf = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < m; ++i) {
        res_buf(i) = result_vec[i];
    }
    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第二部分: 余弦相似度 (V3.3.py 行 376-382)
// ═══════════════════════════════════════════════════════════════

double cosine_similarity(ArrD x_arr, ArrD y_arr) {
    auto x = x_arr.unchecked<1>();
    auto y = y_arr.unchecked<1>();
    py::ssize_t n = x.shape(0);

    if (n != y.shape(0)) {
        throw std::invalid_argument("x and y must have same length");
    }

    const double* xp = x.data(0);
    const double* yp = y.data(0);

    double dot, norm_x2, norm_y2;
    {
        py::gil_scoped_release release;
        dot = 0.0; norm_x2 = 0.0; norm_y2 = 0.0;
        for (py::ssize_t i = 0; i < n; ++i) {
            dot += xp[i] * yp[i];
            norm_x2 += xp[i] * xp[i];
            norm_y2 += yp[i] * yp[i];
        }
    }

    double norm_x = std::sqrt(norm_x2);
    double norm_y = std::sqrt(norm_y2);
    if (norm_x < 1e-12 || norm_y < 1e-12) {
        return 0.0;
    }
    return dot / (norm_x * norm_y);
}

// ═══════════════════════════════════════════════════════════════
// 第三部分: DTW 距离 (V3.3.py 行 339-359)
// ═══════════════════════════════════════════════════════════════

// Span版 DTW 距离（零拷贝 + 滚动双行数组，O(m) 内存）
// 供 public API 和内部批量函数共用
double dtw_distance_span(const double* x, py::ssize_t n,
                          const double* y, py::ssize_t m,
                          int window = 5) {
    if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();

    int band = std::max(window, static_cast<int>(std::abs(n - m)));
    const double INF = std::numeric_limits<double>::infinity();

    std::vector<double> prev(m + 1, INF);
    std::vector<double> curr(m + 1, INF);
    prev[0] = 0.0;

    for (py::ssize_t i = 1; i <= n; ++i) {
        py::ssize_t j_start = std::max(py::ssize_t(1), i - band);
        py::ssize_t j_end = std::min(m, i + band);

        for (py::ssize_t j = j_start; j <= j_end; ++j) {
            double cost = x[i - 1] - y[j - 1];
            cost *= cost;

            double pj = (std::abs((i - 1) - j) <= band) ? prev[j] : INF;
            double cj = (j > j_start) ? curr[j - 1] : INF;
            double pj1 = prev[j - 1];

            curr[j] = cost + std::min({pj, cj, pj1});
        }

        std::swap(prev, curr);
        // dtw[i][0] = INF for all i > 0（prev[0] 经 swap 可能残留 0.0）
        prev[0] = INF;
    }

    double path_len = static_cast<double>(n + m);
    return (path_len > 0) ? std::sqrt(prev[m]) / path_len : INF;
}

double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
    auto x = x_arr.unchecked<1>();
    auto y = y_arr.unchecked<1>();
    py::ssize_t n = x.shape(0);
    py::ssize_t m = y.shape(0);

    if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();

    double result;
    {
        py::gil_scoped_release release;
        result = dtw_distance_span(x.data(0), n, y.data(0), m, window);
    }

    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第四部分: ADX 计算 (V3.3.py 行 757-795)
// ═══════════════════════════════════════════════════════════════

double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
    if (n <= 0) {
        throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
    }
    auto high = high_arr.unchecked<1>();
    auto low  = low_arr.unchecked<1>();
    auto close = close_arr.unchecked<1>();
    py::ssize_t len = high.shape(0);

    if (len < n + 16) return 25.0;
    if (low.shape(0) != len || close.shape(0) != len) {
        throw std::invalid_argument("high/low/close must have same length");
    }

    double result;
    {
        py::gil_scoped_release release;

        py::ssize_t tr_len = len - 1;
        std::vector<double> tr(tr_len), plus_dm(tr_len), minus_dm(tr_len);

        for (py::ssize_t i = 0; i < tr_len; ++i) {
            double hl = high(i + 1) - low(i + 1);
            double hc = std::abs(high(i + 1) - close(i));
            double lc = std::abs(low(i + 1) - close(i));
            tr[i] = std::max({hl, hc, lc});

            double up = high(i + 1) - high(i);
            double down = low(i) - low(i + 1);
            plus_dm[i]  = (up > down && up > 0) ? up : 0.0;
            minus_dm[i] = (down > up && down > 0) ? down : 0.0;
        }

        // Wilder's smoothing
        auto wilder_smooth = [&](const std::vector<double>& raw) {
            std::vector<double> smoothed(tr_len, 0.0);
            double init_sum = 0.0;
            for (int i = 0; i < n; ++i) init_sum += raw[i];
            // Fill first n positions with initial mean (match Python behaviour)
            double init_mean = init_sum / n;
            for (int i = 0; i < n; ++i) smoothed[i] = init_mean;
            for (py::ssize_t i = n; i < tr_len; ++i) {
                smoothed[i] = (smoothed[i - 1] * (n - 1) + raw[i]) / n;
            }
            return smoothed;
        };

        auto atr_s = wilder_smooth(tr);
        auto plus_s = wilder_smooth(plus_dm);
        auto minus_s = wilder_smooth(minus_dm);

        std::vector<double> dx(tr_len);
        for (py::ssize_t i = 0; i < tr_len; ++i) {
            double pdi = 100.0 * plus_s[i] / (atr_s[i] + 1e-12);
            double mdi = 100.0 * minus_s[i] / (atr_s[i] + 1e-12);
            dx[i] = 100.0 * std::abs(pdi - mdi) / (pdi + mdi + 1e-12);
        }

        auto adx_s = wilder_smooth(dx);
        result = adx_s.back();
    }

    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第五部分: ATR 计算
// ═══════════════════════════════════════════════════════════════

ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
    if (n <= 0) {
        throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
    }
    auto high = high_arr.unchecked<1>();
    auto low  = low_arr.unchecked<1>();
    auto close = close_arr.unchecked<1>();
    py::ssize_t len = high.shape(0);

    // v3: 输入校验 (GPT-5.5 最终审查 P0)
    if (low.shape(0) != len || close.shape(0) != len) {
        throw std::invalid_argument("high/low/close must have same length");
    }
    if (len < n + 1) {
        ArrD result(len);
        auto res = result.mutable_unchecked<1>();
        for (py::ssize_t i = 0; i < len; ++i)
            res(i) = std::numeric_limits<double>::quiet_NaN();
        return result;
    }

    const double* hp = high.data(0);
    const double* lp = low.data(0);
    const double* cp = close.data(0);

    ArrD result(len);
    auto res = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < n; ++i) res(i) = std::numeric_limits<double>::quiet_NaN();

    {
        py::gil_scoped_release release;

        py::ssize_t tr_len = len - 1;
        std::vector<double> tr(tr_len);

        for (py::ssize_t i = 0; i < tr_len; ++i) {
            double hl = hp[i + 1] - lp[i + 1];
            double hc = std::abs(hp[i + 1] - cp[i]);
            double lc = std::abs(lp[i + 1] - cp[i]);
            tr[i] = std::max({hl, hc, lc});
        }

        double init_sum = 0.0;
        for (int i = 0; i < n; ++i) init_sum += tr[i];
        res(n) = init_sum / n;

        for (py::ssize_t i = n + 1; i < len; ++i) {
            res(i) = (res(i - 1) * (n - 1) + tr[i - 1]) / n;
        }
    }
    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第六部分: 形态匹配引擎 (V3.3.py 行 389-627)
// ═══════════════════════════════════════════════════════════════

namespace {

struct MatchCandidate {
    py::ssize_t hist_end;
    py::ssize_t hist_start;
    double cos_s;
    std::vector<double> hist_rets;
};

struct PatternResult {
    double top1_sim, top5_avg_sim, sim_decay, sim_variance;
    double match_distance_ratio, avg_future_ret, weighted_future_ret;
    double median_future_ret, ret_sign_consistency, best_match_ret;
    double max_dd_in_matches, match_time_span, match_time_span_ratio;
    double match_cluster_ratio;
    int n_matches_above_thresh;
};

// 从价格数组提取窗口
std::vector<double> extract_window(const double* prices, py::ssize_t start, py::ssize_t end) {
    std::vector<double> result;
    result.reserve(end - start + 1);
    for (py::ssize_t i = start; i <= end; ++i) {
        result.push_back(prices[i]);
    }
    return result;
}

// 向量版余弦相似度（用于批量内部计算）
double cosine_similarity_vec(const std::vector<double>& x, const std::vector<double>& y) {
    py::ssize_t n = static_cast<py::ssize_t>(x.size());
    if (n != static_cast<py::ssize_t>(y.size())) {
        return 0.0;
    }
    if (n == 0) return 0.0;

    double dot = 0.0, norm_x2 = 0.0, norm_y2 = 0.0;
    for (py::ssize_t i = 0; i < n; ++i) {
        dot += x[i] * y[i];
        norm_x2 += x[i] * x[i];
        norm_y2 += y[i] * y[i];
    }
    double norm_x = std::sqrt(norm_x2);
    double norm_y = std::sqrt(norm_y2);
    if (norm_x < 1e-12 || norm_y < 1e-12) {
        return 0.0;
    }
    return dot / (norm_x * norm_y);
}

// 向量版 DTW（兼容旧调用，委托给 span 版）
inline double dtw_distance_vec(const std::vector<double>& x, const std::vector<double>& y, int window = 5) {
    return dtw_distance_span(x.data(), static_cast<py::ssize_t>(x.size()),
                              y.data(), static_cast<py::ssize_t>(y.size()), window);
}

// 批量 DTW: 一个 query 对 N 个 candidates（一对一远端循环，GIL 释放）
py::object dtw_distance_batch(
    ArrD query_arr,
    ArrD candidates_arr,
    int window = 5,
    int top_k = 0
) {
    auto q = query_arr.unchecked<1>();
    auto c = candidates_arr.unchecked<2>();
    py::ssize_t L = q.shape(0);
    py::ssize_t N = c.shape(0);

    if (N == 0) {
        if (top_k > 0) {
            ArrI64 empty_idx(0);
            ArrD empty_dist(0);
            return py::make_tuple(empty_idx, empty_dist);
        }
        ArrD empty_result(0);
        return empty_result;
    }

    if (c.shape(1) != L) {
        throw std::invalid_argument(
            "candidates.shape[1] must equal query length, got " +
            std::to_string(c.shape(1)) + " vs " + std::to_string(L));
    }

    std::vector<double> distances(N);

    {
        py::gil_scoped_release release;
        const double* q_ptr = q.data(0);
        for (py::ssize_t i = 0; i < N; ++i) {
            distances[i] = dtw_distance_span(q_ptr, L, c.data(i, 0), L, window);
        }
    }

    if (top_k <= 0 || top_k >= static_cast<int>(N)) {
        ArrD result(N);
        auto res_buf = result.mutable_unchecked<1>();
        for (py::ssize_t i = 0; i < N; ++i) res_buf(i) = distances[i];
        return result;
    }

    // Top-K via partial_sort
    std::vector<std::pair<double, py::ssize_t>> indexed;
    indexed.reserve(N);
    for (py::ssize_t i = 0; i < N; ++i) {
        indexed.emplace_back(distances[i], i);
    }
    std::partial_sort(
        indexed.begin(),
        indexed.begin() + top_k,
        indexed.end());

    ArrI64 top_indices(top_k);
    ArrD top_dists(top_k);
    auto idx_buf = top_indices.mutable_unchecked<1>();
    auto dist_buf = top_dists.mutable_unchecked<1>();
    for (int i = 0; i < top_k; ++i) {
        idx_buf(i) = static_cast<int64_t>(indexed[i].second);
        dist_buf(i) = indexed[i].first;
    }

    return py::make_tuple(top_indices, top_dists);
}

// 从 Top-K 有效匹配中提取 15 维特征
PatternResult compute_pattern_features_cpp(
    const std::vector<double>& valid_scores,
    const std::vector<double>& valid_frets,
    const std::vector<py::ssize_t>& valid_ends,
    int T_back
) {
    PatternResult r{};
    int top_k_actual = static_cast<int>(valid_scores.size());

    // F1-F5: 相似度特征
    r.top1_sim = valid_scores[0];
    int n_avg = std::min(5, top_k_actual);
    double sum_avg = 0.0;
    for (int i = 0; i < n_avg; ++i) sum_avg += valid_scores[i];
    r.top5_avg_sim = sum_avg / n_avg;
    r.sim_decay = r.top1_sim - r.top5_avg_sim;

    double var = 0.0, mean_s = 0.0;
    for (auto s : valid_scores) mean_s += s;
    mean_s /= top_k_actual;
    for (auto s : valid_scores) var += (s - mean_s) * (s - mean_s);
    r.sim_variance = (top_k_actual > 1) ? var / top_k_actual : 0.0;
    r.match_distance_ratio = (r.top1_sim > 1e-12) ? r.sim_decay / r.top1_sim : 0.0;

    // F6-F11: 后续表现
    double sum_fr = 0.0;
    for (auto fr : valid_frets) sum_fr += fr;
    r.avg_future_ret = sum_fr / top_k_actual;

    double sum_ws = 0.0, sum_w = 0.0;
    for (int i = 0; i < top_k_actual; ++i) {
        sum_ws += valid_scores[i] * valid_frets[i];
        sum_w += valid_scores[i];
    }
    r.weighted_future_ret = (sum_w > 1e-12) ? sum_ws / sum_w : r.avg_future_ret;

    std::vector<double> sorted_fr = valid_frets;
    std::sort(sorted_fr.begin(), sorted_fr.end());
    r.median_future_ret = (top_k_actual % 2 == 1)
        ? sorted_fr[top_k_actual / 2]
        : (sorted_fr[top_k_actual / 2 - 1] + sorted_fr[top_k_actual / 2]) / 2.0;

    int pos_count = 0;
    for (auto fr : valid_frets) if (fr > 0) ++pos_count;
    r.ret_sign_consistency = static_cast<double>(pos_count) / top_k_actual;
    r.best_match_ret = valid_frets[0];

    double min_fr = *std::min_element(valid_frets.begin(), valid_frets.end());
    r.max_dd_in_matches = std::max(0.0, -min_fr);

    // F12-F15: 匹配质量
    auto [min_e, max_e] = std::minmax_element(valid_ends.begin(), valid_ends.end());
    r.match_time_span = static_cast<double>(*max_e - *min_e);
    r.match_time_span_ratio = r.match_time_span / T_back;

    std::vector<py::ssize_t> sorted_ends = valid_ends;
    std::sort(sorted_ends.begin(), sorted_ends.end());
    int max_in_window = 0;
    for (int i = 0; i < top_k_actual; ++i) {
        double target = static_cast<double>(sorted_ends[i]) + 60.0;
        auto it = std::upper_bound(sorted_ends.begin(), sorted_ends.end(),
                                   static_cast<py::ssize_t>(target));
        int count = static_cast<int>(it - sorted_ends.begin()) - i;
        max_in_window = std::max(max_in_window, count);
    }
    r.match_cluster_ratio = static_cast<double>(max_in_window) / top_k_actual;

    int above = 0;
    for (auto s : valid_scores) if (s > 0.8) ++above;
    r.n_matches_above_thresh = above;

    return r;
}

// ═══════════════════════════════════════════════════════════════
// 共享核心：余弦预筛选 → DTW 精排 → 特征提取
// single 和 batch 共用此函数，消除 ~400 行重复逻辑
// ═══════════════════════════════════════════════════════════════
std::optional<PatternResult> pattern_match_core(
    const double* prices, py::ssize_t n_prices,
    int T_idx, int k, int L_query, int T_back,
    int match_step, int M_forward, int dtw_window,
    int cos_prefilter_top,
    const std::vector<double>& query_rets,
    py::ssize_t search_start, py::ssize_t search_end,
    const std::vector<std::vector<double>>* precomputed_rets
) {
    py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());

    // ═══ 第1遍：余弦相似度 + 快速形状距离（全量候选）═══
    std::vector<MatchCandidate> cos_candidates;
    std::vector<double> fast_shape_dists;

    for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
        py::ssize_t hist_start = hist_end - L_query + 1;
        if (hist_start < 0) continue;

        // 获取标准化收益率：缓存优先，否则现场计算
        const std::vector<double>* hist_rets_ptr = nullptr;
        std::vector<double> hist_rets_scratch;

        if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size())) {
            hist_rets_ptr = &(*precomputed_rets)[hist_end];
        } else {
            auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
            if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
                hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query);
                hist_rets_ptr = &hist_rets_scratch;
            }
        }

        if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;

        const auto& hist_rets = *hist_rets_ptr;

        // 余弦相似度
        double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
        py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
        for (py::ssize_t i = 0; i < min_len; ++i) {
            dot += hist_rets[i] * query_rets[i];
            nx2 += hist_rets[i] * hist_rets[i];
            ny2 += query_rets[i] * query_rets[i];
        }
        double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
        double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;

        // 快速形状距离
        double fast_d2 = 0.0;
        for (py::ssize_t i = 0; i < min_len; ++i) {
            double diff = hist_rets[i] - query_rets[i];
            fast_d2 += diff * diff;
        }
        fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));

        if (cos_s > 0) {
            cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
        }
    }

    if (cos_candidates.size() < 3) return std::nullopt;

    // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
    double sigma_fast = 1.0;
    if (fast_shape_dists.size() > 1) {
        double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0.0)
                        / fast_shape_dists.size();
        double var_fd = 0.0;
        for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
        var_fd /= fast_shape_dists.size();
        sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)));
    }
    sigma_fast = std::max(sigma_fast, 1e-12);

    // 余弦排序 + 全量边界
    std::sort(cos_candidates.begin(), cos_candidates.end(),
              [](const MatchCandidate& a, const MatchCandidate& b) { return a.cos_s > b.cos_s; });

    double global_min_cos = cos_candidates.back().cos_s;
    double global_max_cos = cos_candidates.front().cos_s;

    int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
    cos_candidates.resize(n_cos);

    // ═══ 第2遍：DTW 精排 (仅 top-N) ═══
    std::vector<double> dtw_dists, cos_sims, future_rets;
    std::vector<py::ssize_t> match_ends;
    dtw_dists.reserve(n_cos);
    cos_sims.reserve(n_cos);
    future_rets.reserve(n_cos);
    match_ends.reserve(n_cos);

    for (const auto& cand : cos_candidates) {
        py::ssize_t hn = static_cast<py::ssize_t>(cand.hist_rets.size());
        double dtw_d = dtw_distance_span(cand.hist_rets.data(), hn,
                                          query_rets.data(), n_query, dtw_window);

        dtw_dists.push_back(dtw_d);
        cos_sims.push_back(cand.cos_s);

        py::ssize_t fut_end = cand.hist_end + M_forward;
        if (fut_end < n_prices && fut_end < T_idx) {
            future_rets.push_back(prices[fut_end] / prices[cand.hist_end] - 1.0);
        } else {
            future_rets.push_back(std::numeric_limits<double>::quiet_NaN());
        }
        match_ends.push_back(cand.hist_end);
    }

    if (dtw_dists.size() < 3) return std::nullopt;

    // sim_dtw = exp(-dtw/sigma)
    double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;

    std::vector<double> sim_dtw(dtw_dists.size());
    double min_dtw_v = std::numeric_limits<double>::max();
    double max_dtw_v = std::numeric_limits<double>::lowest();
    for (size_t i = 0; i < dtw_dists.size(); ++i) {
        sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
        min_dtw_v = std::min(min_dtw_v, sim_dtw[i]);
        max_dtw_v = std::max(max_dtw_v, sim_dtw[i]);
    }

    // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
    double range_dtw = (max_dtw_v - min_dtw_v > 1e-12) ? (max_dtw_v - min_dtw_v) : 1.0;
    double range_cos_val = (global_max_cos - global_min_cos > 1e-12)
                           ? (global_max_cos - global_min_cos) : 1.0;

    struct Scored { double score, fut_ret; py::ssize_t end_idx; };
    std::vector<Scored> scored;
    scored.reserve(sim_dtw.size());
    for (size_t i = 0; i < sim_dtw.size(); ++i) {
        double nd = (sim_dtw[i] - min_dtw_v) / range_dtw;
        double nc = (cos_sims[i] - global_min_cos) / range_cos_val;
        scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
    }

    std::sort(scored.begin(), scored.end(),
              [](const Scored& a, const Scored& b) { return a.score > b.score; });

    int top_k = std::min(k, static_cast<int>(scored.size()));

    // 过滤 NaN 未来收益
    std::vector<double> valid_scores, valid_frets;
    std::vector<py::ssize_t> valid_ends;
    for (int i = 0; i < top_k; ++i) {
        if (!std::isnan(scored[i].fut_ret)) {
            valid_scores.push_back(scored[i].score);
            valid_frets.push_back(scored[i].fut_ret);
            valid_ends.push_back(scored[i].end_idx);
        }
    }
    if (valid_scores.size() < 2) return std::nullopt;

    return compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);
}

} // namespace

// ═══════════════════════════════════════════════════════════════
// 第六部分-A: 单点形态匹配（薄包装 → pattern_match_core）
// ═══════════════════════════════════════════════════════════════
py::object pattern_match_single(
    ArrD prices_arr,
    int T_idx,
    int k = 10,
    int L_query = 20,
    int T_back = 750,
    int match_step = 1,
    int M_forward = 5,
    int dtw_window = 5,
    int cos_prefilter_top = 50
) {
    auto prices_buf = prices_arr.unchecked<1>();
    py::ssize_t n_prices = prices_buf.shape(0);
    const double* prices = prices_buf.data(0);

    // ── 输入校验 ──
    if (T_idx < 0 || static_cast<py::ssize_t>(T_idx) >= n_prices) {
        throw std::out_of_range("T_idx must satisfy 0 <= T_idx < len(prices), got " + std::to_string(T_idx));
    }
    if (L_query < 3) {
        throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
    }
    if (T_back <= 0) {
        throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
    }
    if (k <= 0) {
        throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
    }
    if (M_forward < 1) {
        throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
    }
    if (match_step <= 0) {
        throw std::invalid_argument("match_step must be > 0");
    }
    if (dtw_window < 0) {
        throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
    }
    if (cos_prefilter_top <= 0) {
        throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
    }
    if (T_idx < L_query + M_forward + 10) return py::none();
    if (T_idx - L_query + 1 < 0) return py::none();

    // 查询窗口标准化
    auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
    if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) return py::none();

    std::vector<double> query_rets;
    {
        py::gil_scoped_release release;
        query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
    }
    if (query_rets.size() < 2) return py::none();

    py::ssize_t search_end = T_idx - L_query;
    if (search_end < L_query) return py::none();
    py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
                                        py::ssize_t(T_idx - T_back));

    // ── 委托共享核心（无预计算缓存，现场标准化）──
    std::optional<PatternResult> result_opt;
    {
        py::gil_scoped_release release;
        result_opt = pattern_match_core(
            prices, n_prices, T_idx, k, L_query, T_back,
            match_step, M_forward, dtw_window, cos_prefilter_top,
            query_rets, search_start, search_end,
            nullptr  // 无预计算缓存
        );
    }

    if (!result_opt.has_value()) return py::none();

    // ── 构造返回值 ──
    py::dict result;
    result["top1_sim"] = result_opt->top1_sim;
    result["top5_avg_sim"] = result_opt->top5_avg_sim;
    result["sim_decay"] = result_opt->sim_decay;
    result["sim_variance"] = result_opt->sim_variance;
    result["match_distance_ratio"] = result_opt->match_distance_ratio;
    result["avg_future_ret"] = result_opt->avg_future_ret;
    result["weighted_future_ret"] = result_opt->weighted_future_ret;
    result["median_future_ret"] = result_opt->median_future_ret;
    result["ret_sign_consistency"] = result_opt->ret_sign_consistency;
    result["best_match_ret"] = result_opt->best_match_ret;
    result["max_dd_in_matches"] = result_opt->max_dd_in_matches;
    result["match_time_span"] = result_opt->match_time_span;
    result["match_time_span_ratio"] = result_opt->match_time_span_ratio;
    result["match_cluster_ratio"] = result_opt->match_cluster_ratio;
    result["n_matches_above_thresh"] = result_opt->n_matches_above_thresh;
    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第七部分: 批量形态匹配 (v3 新增)
// ═══════════════════════════════════════════════════════════════

py::tuple pattern_match_batch(
    ArrD prices_arr,
    ArrI64 t_indices_arr,
    int k = 10,
    int L_query = 20,
    int T_back = 750,
    int match_step = 1,
    int M_forward = 5,
    int dtw_window = 5,
    int cos_prefilter_top = 50
) {
    auto prices_buf = prices_arr.unchecked<1>();
    py::ssize_t n_prices = prices_buf.shape(0);
    const double* prices = prices_buf.data(0);

    auto t_buf = t_indices_arr.unchecked<1>();
    py::ssize_t n_samples = t_buf.shape(0);
    const int64_t* t_ptr = t_buf.data(0);

    // ── 输入校验 ──
    if (L_query < 3) {
        throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
    }
    if (T_back <= 0) {
        throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
    }
    if (k <= 0) {
        throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
    }
    if (M_forward < 1) {
        throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
    }
    if (match_step <= 0) {
        throw std::invalid_argument("match_step must be > 0");
    }
    if (dtw_window < 0) {
        throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
    }
    if (cos_prefilter_top <= 0) {
        throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
    }
    if (n_samples == 0) {
        ArrD empty_features(std::vector<py::ssize_t>{0, 15});
        py::array_t<bool> empty_mask(std::vector<py::ssize_t>{0});
        return py::make_tuple(empty_features, empty_mask);
    }

    for (py::ssize_t i = 1; i < n_samples; ++i) {
        if (t_ptr[i] <= t_ptr[i - 1]) {
            throw std::invalid_argument("t_indices must be strictly increasing");
        }
    }
    if (t_ptr[n_samples - 1] >= n_prices) {
        throw std::invalid_argument("max(t_indices) must be < len(prices)");
    }

    std::vector<double> features_flat;
    features_flat.reserve(n_samples * 15);
    std::vector<bool> valid_mask(n_samples, false);

    {
        // ── GIL 释放区：纯 C++ 批量计算 ──
        py::gil_scoped_release release;

        // ── 第一遍：计算所有 T_idx 搜索范围的并集（避免预计算无用窗口）──
        py::ssize_t precompute_start = n_prices;
        py::ssize_t precompute_end = 0;
        for (py::ssize_t s = 0; s < n_samples; ++s) {
            int T_idx = static_cast<int>(t_ptr[s]);
            if (T_idx < L_query + M_forward + 10) continue;
            py::ssize_t s_end = T_idx - L_query;
            if (s_end < L_query) continue;
            py::ssize_t s_start = std::max(py::ssize_t(L_query - 1),
                                           py::ssize_t(T_idx - T_back));
            if (s_start < s_end) {
                precompute_start = std::min(precompute_start, s_start);
                precompute_end = std::max(precompute_end, s_end);
            }
        }

        // ── 仅预计算搜索范围并集内的窗口标准化收益率 ──
        std::vector<std::vector<double>> precomputed_rets(n_prices);
        if (precompute_start <= precompute_end) {
            for (py::ssize_t end = precompute_start; end <= precompute_end; ++end) {
                py::ssize_t start = end - L_query + 1;
                if (start >= 0) {
                    auto window_prices = extract_window(prices, start, end);
                    precomputed_rets[end] = standardize_returns_cpp(window_prices.data(), L_query);
                }
            }
        }

        // ── 对每个 T_idx 执行形态匹配（复用预计算缓存）──
        for (py::ssize_t s = 0; s < n_samples; ++s) {
            int T_idx = static_cast<int>(t_ptr[s]);

            if (T_idx < L_query + M_forward + 10) continue;
            if (T_idx - L_query + 1 < 0) continue;

            auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
            if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) continue;

            auto query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
            if (query_rets.size() < 2) continue;

            py::ssize_t search_end = T_idx - L_query;
            if (search_end < L_query) continue;
            py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
                                                py::ssize_t(T_idx - T_back));

            // ── 委托共享核心（使用预计算缓存）──
            auto result_opt = pattern_match_core(
                prices, n_prices, T_idx, k, L_query, T_back,
                match_step, M_forward, dtw_window, cos_prefilter_top,
                query_rets, search_start, search_end,
                &precomputed_rets
            );

            if (!result_opt.has_value()) continue;

            auto& r = *result_opt;
            features_flat.push_back(r.top1_sim);
            features_flat.push_back(r.top5_avg_sim);
            features_flat.push_back(r.sim_decay);
            features_flat.push_back(r.sim_variance);
            features_flat.push_back(r.match_distance_ratio);
            features_flat.push_back(r.avg_future_ret);
            features_flat.push_back(r.weighted_future_ret);
            features_flat.push_back(r.median_future_ret);
            features_flat.push_back(r.ret_sign_consistency);
            features_flat.push_back(r.best_match_ret);
            features_flat.push_back(r.max_dd_in_matches);
            features_flat.push_back(r.match_time_span);
            features_flat.push_back(r.match_time_span_ratio);
            features_flat.push_back(r.match_cluster_ratio);
            features_flat.push_back(static_cast<double>(r.n_matches_above_thresh));

            valid_mask[s] = true;
        }
    } // GIL 在此重新获取

    // ── 构造返回数组 ──
    py::ssize_t n_valid = static_cast<py::ssize_t>(features_flat.size()) / 15;
    ArrD features_X15(std::vector<py::ssize_t>{n_valid, 15});
    auto fx_buf = features_X15.mutable_unchecked<2>();
    for (py::ssize_t i = 0; i < n_valid; ++i) {
        for (py::ssize_t j = 0; j < 15; ++j) {
            fx_buf(i, j) = features_flat[i * 15 + j];
        }
    }

    py::array_t<bool> valid_mask_arr(std::vector<py::ssize_t>{n_samples});
    auto vm_buf = valid_mask_arr.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < n_samples; ++i) {
        vm_buf(i) = valid_mask[i];
    }

    return py::make_tuple(features_X15, valid_mask_arr);
}

// ═══════════════════════════════════════════════════════════════
// 模块定义
// ═══════════════════════════════════════════════════════════════

PYBIND11_MODULE(etf_core, m) {
    m.doc() = "ETF pattern matching core — C++ accelerated (pybind11)\n\n"
              "来源: 形态匹配ETF组合策略_V3.3.py\n"
              "模块: dtw_distance, standardize_returns, cosine_similarity,\n"
              "       compute_adx, compute_atr, dtw_distance_batch,\n"
              "       pattern_match_single, pattern_match_batch\n"
              "v2: 三模块合并为单一 etf_core, /utf-8, py::ssize_t, forcecast\n"
              "v3: 新增 pattern_match_batch，支持同 ETF 多 T_idx 批量形态匹配";

    // ── 序列预处理 ──
    m.def("standardize_returns", &standardize_returns,
          py::arg("price_series"),
          "计算标准化收益率序列: (rets - mean) / std.\n\n"
          "Args: price_series (1-D float64 array, n>=2)\n"
          "Returns: 1-D float64 array (length n-1)");

    m.def("cosine_similarity", &cosine_similarity,
          py::arg("x"), py::arg("y"),
          "两向量余弦相似度 ∈ [-1, 1].\n"
          "norm < 1e-12 时返回 0.0.");

    // ── DTW ──
    m.def("dtw_distance", &dtw_distance,
          py::arg("x"), py::arg("y"), py::arg("window") = 5,
          "Sakoe-Chiba band DTW 距离.\n"
          "返回归一化距离: sqrt(dtw[n,m]) / (n+m).\n"
          "空序列返回 inf.");

    m.def("dtw_distance_batch", &dtw_distance_batch,
          py::arg("query"), py::arg("candidates"),
          py::arg("window") = 5, py::arg("top_k") = 0,
          "批量 DTW: 一个 query 对 N 个 candidates.\n\n"
          "Args:\n"
          "  query: 1-D float64 array (L,)\n"
          "  candidates: 2-D float64 array (N, L)\n"
          "  window: Sakoe-Chiba band 宽度\n"
          "  top_k: 若 >0 且 <N，返回 (top_indices, top_distances);\n"
          "         否则返回全部 distances (N,)\n\n"
          "Returns: distances (N,) 或 (indices, distances) 各 (top_k,)");

    // ── 技术指标 ──
    m.def("compute_adx", &compute_adx,
          py::arg("high"), py::arg("low"), py::arg("close"),
          py::arg("n") = 14,
          "ADX (Average Directional Index), Wilder's smoothing.\n"
          "数据不足时返回 25.0 (中性值).");

    m.def("compute_atr", &compute_atr,
          py::arg("high"), py::arg("low"), py::arg("close"),
          py::arg("n") = 14,
          "ATR (Average True Range).\n"
          "前 n 天为 NaN.");

    // 模块常量：15 维特征名（顺序与 pattern_match_batch 的 features_X15 列一致）
    m.attr("FEATURE_KEYS") = py::make_tuple(
        "top1_sim",
        "top5_avg_sim",
        "sim_decay",
        "sim_variance",
        "match_distance_ratio",
        "avg_future_ret",
        "weighted_future_ret",
        "median_future_ret",
        "ret_sign_consistency",
        "best_match_ret",
        "max_dd_in_matches",
        "match_time_span",
        "match_time_span_ratio",
        "match_cluster_ratio",
        "n_matches_above_thresh"
    );

    // ── 形态匹配 ──
    m.def("pattern_match_single", &pattern_match_single,
          py::arg("prices"),
          py::arg("T_idx"),
          py::arg("k") = 10,
          py::arg("L_query") = 20,
          py::arg("T_back") = 750,
          py::arg("match_step") = 1,
          py::arg("M_forward") = 5,
          py::arg("dtw_window") = 5,
          py::arg("cos_prefilter_top") = 50,
          "单 ETF 单时点形态匹配 → 15维特征字典.\n\n"
          "V3.0 余弦预筛选: 第1遍全量余弦 → 第2遍 DTW 精排.\n"
          "前视偏差防护: fut_end < T_idx 严格约束.\n"
          "数据不足返回 None.\n\n"
          "Returns: dict with 15 keys or None.\n"
          "  F1-F5:  top1_sim, top5_avg_sim, sim_decay, sim_variance, match_distance_ratio\n"
          "  F6-F11: avg_future_ret, weighted_future_ret, median_future_ret,\n"
          "          ret_sign_consistency, best_match_ret, max_dd_in_matches\n"
          "  F12-F15: match_time_span, match_time_span_ratio, match_cluster_ratio,\n"
          "           n_matches_above_thresh");

    m.def("pattern_match_batch", &pattern_match_batch,
          py::arg("prices"), py::arg("t_indices"),
          py::arg("k") = 10, py::arg("L_query") = 20,
          py::arg("T_back") = 750, py::arg("match_step") = 1,
          py::arg("M_forward") = 5, py::arg("dtw_window") = 5,
          py::arg("cos_prefilter_top") = 50,
          "批量形态匹配——同ETF多T_idx.\n\n"
          "核心优化: 候选窗口标准化收益率在相邻 T_idx 之间高度重叠，\n"
          "C++ 内部一次性预计算并复用，避免 Python 往返和重复标准化.\n\n"
          "Returns: (features_X15, valid_mask).\n"
          "features_X15: (n_valid, 15) float64 — 仅有效样本.\n"
          "valid_mask: (n_samples,) bool.\n"
          "feature_keys 已提升为模块常量 etf_core.FEATURE_KEYS (15 str).");
}

--- src/cpp/CMakeLists.txt ---
# C++ 加速模块 — 统一 etf_core 模块
# v2 修订：三模块合并为一个，减少 ABI 管理复杂度和重复样板代码
# v3: 固定输出到 build/ (MSVC 加 config 子目录 → build/Release/)

pybind11_add_module(etf_core MODULE etf_core.cpp)
set_target_properties(etf_core PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)
message(STATUS "C++ module: etf_core")

--- root CMakeLists.txt ---
cmake_minimum_required(VERSION 3.20)

# ──────────────────────────────────────────────
# 形态匹配ETF策略 — C++ 加速模块
# > 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
# > 复用 pybind11-demo 已验证的 MSVC 配置
# > v2: 三模块合并为单 etf_core, /utf-8 优先
# ──────────────────────────────────────────────

project(etf_pattern_match LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Python
set(Python_EXECUTABLE "" CACHE FILEPATH "Path to python.exe")
if(Python_EXECUTABLE)
    get_filename_component(Python_ROOT_DIR "${Python_EXECUTABLE}" DIRECTORY)
endif()
if(NOT Python_EXECUTABLE)
    message(WARNING
        "Python_EXECUTABLE not set. "
        "Use -DPython_EXECUTABLE=/path/to/python.exe to specify which Python to use.\n"
        "  Example: cmake -B build -DPython_EXECUTABLE=<path-to-python.exe>")
endif()
find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Module)

# pybind11 — auto-detect
set(pybind11_DIR "" CACHE PATH "pybind11 cmake config dir")
if(NOT pybind11_DIR)
    execute_process(
        COMMAND "${Python_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE _pybind11_cmake_dir OUTPUT_STRIP_TRAILING_WHITESPACE ERROR_QUIET
    )
    if(_pybind11_cmake_dir)
        set(pybind11_DIR "${_pybind11_cmake_dir}")
    endif()
endif()
if(NOT pybind11_DIR)
    message(FATAL_ERROR
        "pybind11 not found!\n"
        "  Install: pip install pybind11\n"
        "  Verify:  python -c \"import pybind11; print(pybind11.__version__)\"\n"
        "  Or set:  -Dpybind11_DIR=/path/to/share/cmake/pybind11\n"
        "  Or set:  -DPython_EXECUTABLE=/path/to/python.exe (auto-detect uses this Python)")
endif()
find_package(pybind11 REQUIRED CONFIG)

# MSVC — v2: 优先 /utf-8，/wd4819 为后备
if(MSVC)
    add_compile_options("$<$<CONFIG:Release>:/O2>")
    add_compile_options(/utf-8 /wd4819)
endif()

# 子目录 — C++ 模块
add_subdirectory(src/cpp)

# Install — scikit-build-core 需要这些指令来打包 wheel
install(TARGETS etf_core DESTINATION src/cpp)
# Also expose the extension at the top level for ``import etf_core`` after pip install.
install(TARGETS etf_core DESTINATION .)
# Match scikit-build-core's wheel package destination (``cpp``) as well.
install(TARGETS etf_core DESTINATION cpp)




exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Output '"'--- function definitions ---'; Select-String -Path 'src/cpp/etf_core.cpp' -Encoding UTF8 -Pattern '"'^(ArrD|double|py::object|py::tuple) (standardize_returns|cosine_similarity|dtw_distance|dtw_distance_batch|compute_adx|compute_atr|pattern_match_single|pattern_match_batch)'"\\b' -Context 0,3; Write-Output '--- tests directory ---'; Get-ChildItem -Force 'tests'; Write-Output '--- git status ---'; git status --short" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 238ms:
--- function definitions ---

> src\cpp\etf_core.cpp:104:ArrD standardize_returns(ArrD price_series) {
  src\cpp\etf_core.cpp:105:    auto buf = price_series.unchecked<1>();
  src\cpp\etf_core.cpp:106:    py::ssize_t n = buf.shape(0);
  src\cpp\etf_core.cpp:107:    const double* ptr = buf.data(0);
> src\cpp\etf_core.cpp:128:double cosine_similarity(ArrD x_arr, ArrD y_arr) {
  src\cpp\etf_core.cpp:129:    auto x = x_arr.unchecked<1>();
  src\cpp\etf_core.cpp:130:    auto y = y_arr.unchecked<1>();
  src\cpp\etf_core.cpp:131:    py::ssize_t n = x.shape(0);
> src\cpp\etf_core.cpp:201:double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
  src\cpp\etf_core.cpp:202:    auto x = x_arr.unchecked<1>();
  src\cpp\etf_core.cpp:203:    auto y = y_arr.unchecked<1>();
  src\cpp\etf_core.cpp:204:    py::ssize_t n = x.shape(0);
> src\cpp\etf_core.cpp:222:double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
  src\cpp\etf_core.cpp:223:    if (n <= 0) {
  src\cpp\etf_core.cpp:224:        throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
  src\cpp\etf_core.cpp:225:    }
> src\cpp\etf_core.cpp:291:ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
  src\cpp\etf_core.cpp:292:    if (n <= 0) {
  src\cpp\etf_core.cpp:293:        throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
  src\cpp\etf_core.cpp:294:    }
> src\cpp\etf_core.cpp:405:py::object dtw_distance_batch(
  src\cpp\etf_core.cpp:406:    ArrD query_arr,
  src\cpp\etf_core.cpp:407:    ArrD candidates_arr,
  src\cpp\etf_core.cpp:408:    int window = 5,
> src\cpp\etf_core.cpp:714:py::object pattern_match_single(
  src\cpp\etf_core.cpp:715:    ArrD prices_arr,
  src\cpp\etf_core.cpp:716:    int T_idx,
  src\cpp\etf_core.cpp:717:    int k = 10,
> src\cpp\etf_core.cpp:811:py::tuple pattern_match_batch(
  src\cpp\etf_core.cpp:812:    ArrD prices_arr,
  src\cpp\etf_core.cpp:813:    ArrI64 t_indices_arr,
  src\cpp\etf_core.cpp:814:    int k = 10,
--- tests directory ---

PSPath            : Microsoft.PowerShell.Core\FileSystem::E:\workspace\projects\形态匹配ETF策略-pybind11\tests\__pycache__
PSParentPath      : Microsoft.PowerShell.Core\FileSystem::E:\workspace\projects\形态匹配ETF策略-pybind11\tests
PSChildName       : __pycache__
PSDrive           : E
PSProvider        : Microsoft.PowerShell.Core\FileSystem
PSIsContainer     : True
Name              : __pycache__
FullName          : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\__pycache__
Parent            : tests
Exists            : True
Root              : E:\
Extension         : 
CreationTime      : 2026/7/3 21:42:27
CreationTimeUtc   : 2026/7/3 13:42:27
LastAccessTime    : 2026/7/17 17:29:17
LastAccessTimeUtc : 2026/7/17 9:29:17
LastWriteTime     : 2026/7/12 19:41:50
LastWriteTimeUtc  : 2026/7/12 11:41:50
Attributes        : Directory
Mode              : d-----
BaseName          : __pycache__
Target            : {}
LinkType          : 


LastWriteTime : 2026/7/12 19:41:48
Length        : 8532
Name          : test_dtw.py


LastWriteTime : 2026/7/3 23:02:15
Length        : 9229
Name          : test_pattern_match.py


LastWriteTime : 2026/7/4 13:17:33
Length        : 5406
Name          : test_technical.py

--- git status ---
 M project_status.md
?? _review/
?? docs/reviews/performance-analysis-review-kimi.md
?? improvement_plan.md
?? notebooks/01_price_series.png
?? notebooks/02_query_window.png
?? notebooks/03_cosine_prefilter.png
?? notebooks/04_dtw_warping.png
?? notebooks/05_feature_evolution.png
?? notebooks/06_trading_signals.png
?? notebooks/07_batch_dtw.png
?? notebooks/08_benchmark.png
?? prompt_p0_build.md
?? prompt_p1_benchmark.md



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 '"'src/cpp/etf_core.cpp'; foreach ("'$range in @(@(90,335), @(385,475), @(475,735), @(735,910))) { $start=$range[0]; $end=$range[1]; Write-Output "--- lines $start-$end ---"; for ($i=$start; $i -le $end; $i++) { '"'{0,4}: {1}' -f "'$i, $lines[$i-1] } }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 282ms:
--- lines 90-335 ---
  90:     // 标准差
  91:     double sq_sum = 0.0;
  92:     for (auto r : rets) sq_sum += r * r;
  93:     double std_val = std::sqrt(sq_sum / rets.size());
  94: 
  95:     if (std_val < 1e-12) {
  96:         return rets;  // 已去均值，不再除以 std
  97:     }
  98: 
  99:     for (auto& r : rets) r /= std_val;
 100:     return rets;
 101: }
 102: 
 103: // Python 绑定包装
 104: ArrD standardize_returns(ArrD price_series) {
 105:     auto buf = price_series.unchecked<1>();
 106:     py::ssize_t n = buf.shape(0);
 107:     const double* ptr = buf.data(0);
 108: 
 109:     std::vector<double> result_vec;
 110:     {
 111:         py::gil_scoped_release release;
 112:         result_vec = standardize_returns_cpp(ptr, n);
 113:     }
 114: 
 115:     py::ssize_t m = static_cast<py::ssize_t>(result_vec.size());
 116:     ArrD result(m);
 117:     auto res_buf = result.mutable_unchecked<1>();
 118:     for (py::ssize_t i = 0; i < m; ++i) {
 119:         res_buf(i) = result_vec[i];
 120:     }
 121:     return result;
 122: }
 123: 
 124: // ═══════════════════════════════════════════════════════════════
 125: // 第二部分: 余弦相似度 (V3.3.py 行 376-382)
 126: // ═══════════════════════════════════════════════════════════════
 127: 
 128: double cosine_similarity(ArrD x_arr, ArrD y_arr) {
 129:     auto x = x_arr.unchecked<1>();
 130:     auto y = y_arr.unchecked<1>();
 131:     py::ssize_t n = x.shape(0);
 132: 
 133:     if (n != y.shape(0)) {
 134:         throw std::invalid_argument("x and y must have same length");
 135:     }
 136: 
 137:     const double* xp = x.data(0);
 138:     const double* yp = y.data(0);
 139: 
 140:     double dot, norm_x2, norm_y2;
 141:     {
 142:         py::gil_scoped_release release;
 143:         dot = 0.0; norm_x2 = 0.0; norm_y2 = 0.0;
 144:         for (py::ssize_t i = 0; i < n; ++i) {
 145:             dot += xp[i] * yp[i];
 146:             norm_x2 += xp[i] * xp[i];
 147:             norm_y2 += yp[i] * yp[i];
 148:         }
 149:     }
 150: 
 151:     double norm_x = std::sqrt(norm_x2);
 152:     double norm_y = std::sqrt(norm_y2);
 153:     if (norm_x < 1e-12 || norm_y < 1e-12) {
 154:         return 0.0;
 155:     }
 156:     return dot / (norm_x * norm_y);
 157: }
 158: 
 159: // ═══════════════════════════════════════════════════════════════
 160: // 第三部分: DTW 距离 (V3.3.py 行 339-359)
 161: // ═══════════════════════════════════════════════════════════════
 162: 
 163: // Span版 DTW 距离（零拷贝 + 滚动双行数组，O(m) 内存）
 164: // 供 public API 和内部批量函数共用
 165: double dtw_distance_span(const double* x, py::ssize_t n,
 166:                           const double* y, py::ssize_t m,
 167:                           int window = 5) {
 168:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 169: 
 170:     int band = std::max(window, static_cast<int>(std::abs(n - m)));
 171:     const double INF = std::numeric_limits<double>::infinity();
 172: 
 173:     std::vector<double> prev(m + 1, INF);
 174:     std::vector<double> curr(m + 1, INF);
 175:     prev[0] = 0.0;
 176: 
 177:     for (py::ssize_t i = 1; i <= n; ++i) {
 178:         py::ssize_t j_start = std::max(py::ssize_t(1), i - band);
 179:         py::ssize_t j_end = std::min(m, i + band);
 180: 
 181:         for (py::ssize_t j = j_start; j <= j_end; ++j) {
 182:             double cost = x[i - 1] - y[j - 1];
 183:             cost *= cost;
 184: 
 185:             double pj = (std::abs((i - 1) - j) <= band) ? prev[j] : INF;
 186:             double cj = (j > j_start) ? curr[j - 1] : INF;
 187:             double pj1 = prev[j - 1];
 188: 
 189:             curr[j] = cost + std::min({pj, cj, pj1});
 190:         }
 191: 
 192:         std::swap(prev, curr);
 193:         // dtw[i][0] = INF for all i > 0（prev[0] 经 swap 可能残留 0.0）
 194:         prev[0] = INF;
 195:     }
 196: 
 197:     double path_len = static_cast<double>(n + m);
 198:     return (path_len > 0) ? std::sqrt(prev[m]) / path_len : INF;
 199: }
 200: 
 201: double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
 202:     auto x = x_arr.unchecked<1>();
 203:     auto y = y_arr.unchecked<1>();
 204:     py::ssize_t n = x.shape(0);
 205:     py::ssize_t m = y.shape(0);
 206: 
 207:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 208: 
 209:     double result;
 210:     {
 211:         py::gil_scoped_release release;
 212:         result = dtw_distance_span(x.data(0), n, y.data(0), m, window);
 213:     }
 214: 
 215:     return result;
 216: }
 217: 
 218: // ═══════════════════════════════════════════════════════════════
 219: // 第四部分: ADX 计算 (V3.3.py 行 757-795)
 220: // ═══════════════════════════════════════════════════════════════
 221: 
 222: double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 223:     if (n <= 0) {
 224:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 225:     }
 226:     auto high = high_arr.unchecked<1>();
 227:     auto low  = low_arr.unchecked<1>();
 228:     auto close = close_arr.unchecked<1>();
 229:     py::ssize_t len = high.shape(0);
 230: 
 231:     if (len < n + 16) return 25.0;
 232:     if (low.shape(0) != len || close.shape(0) != len) {
 233:         throw std::invalid_argument("high/low/close must have same length");
 234:     }
 235: 
 236:     double result;
 237:     {
 238:         py::gil_scoped_release release;
 239: 
 240:         py::ssize_t tr_len = len - 1;
 241:         std::vector<double> tr(tr_len), plus_dm(tr_len), minus_dm(tr_len);
 242: 
 243:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 244:             double hl = high(i + 1) - low(i + 1);
 245:             double hc = std::abs(high(i + 1) - close(i));
 246:             double lc = std::abs(low(i + 1) - close(i));
 247:             tr[i] = std::max({hl, hc, lc});
 248: 
 249:             double up = high(i + 1) - high(i);
 250:             double down = low(i) - low(i + 1);
 251:             plus_dm[i]  = (up > down && up > 0) ? up : 0.0;
 252:             minus_dm[i] = (down > up && down > 0) ? down : 0.0;
 253:         }
 254: 
 255:         // Wilder's smoothing
 256:         auto wilder_smooth = [&](const std::vector<double>& raw) {
 257:             std::vector<double> smoothed(tr_len, 0.0);
 258:             double init_sum = 0.0;
 259:             for (int i = 0; i < n; ++i) init_sum += raw[i];
 260:             // Fill first n positions with initial mean (match Python behaviour)
 261:             double init_mean = init_sum / n;
 262:             for (int i = 0; i < n; ++i) smoothed[i] = init_mean;
 263:             for (py::ssize_t i = n; i < tr_len; ++i) {
 264:                 smoothed[i] = (smoothed[i - 1] * (n - 1) + raw[i]) / n;
 265:             }
 266:             return smoothed;
 267:         };
 268: 
 269:         auto atr_s = wilder_smooth(tr);
 270:         auto plus_s = wilder_smooth(plus_dm);
 271:         auto minus_s = wilder_smooth(minus_dm);
 272: 
 273:         std::vector<double> dx(tr_len);
 274:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 275:             double pdi = 100.0 * plus_s[i] / (atr_s[i] + 1e-12);
 276:             double mdi = 100.0 * minus_s[i] / (atr_s[i] + 1e-12);
 277:             dx[i] = 100.0 * std::abs(pdi - mdi) / (pdi + mdi + 1e-12);
 278:         }
 279: 
 280:         auto adx_s = wilder_smooth(dx);
 281:         result = adx_s.back();
 282:     }
 283: 
 284:     return result;
 285: }
 286: 
 287: // ═══════════════════════════════════════════════════════════════
 288: // 第五部分: ATR 计算
 289: // ═══════════════════════════════════════════════════════════════
 290: 
 291: ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 292:     if (n <= 0) {
 293:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 294:     }
 295:     auto high = high_arr.unchecked<1>();
 296:     auto low  = low_arr.unchecked<1>();
 297:     auto close = close_arr.unchecked<1>();
 298:     py::ssize_t len = high.shape(0);
 299: 
 300:     // v3: 输入校验 (GPT-5.5 最终审查 P0)
 301:     if (low.shape(0) != len || close.shape(0) != len) {
 302:         throw std::invalid_argument("high/low/close must have same length");
 303:     }
 304:     if (len < n + 1) {
 305:         ArrD result(len);
 306:         auto res = result.mutable_unchecked<1>();
 307:         for (py::ssize_t i = 0; i < len; ++i)
 308:             res(i) = std::numeric_limits<double>::quiet_NaN();
 309:         return result;
 310:     }
 311: 
 312:     const double* hp = high.data(0);
 313:     const double* lp = low.data(0);
 314:     const double* cp = close.data(0);
 315: 
 316:     ArrD result(len);
 317:     auto res = result.mutable_unchecked<1>();
 318:     for (py::ssize_t i = 0; i < n; ++i) res(i) = std::numeric_limits<double>::quiet_NaN();
 319: 
 320:     {
 321:         py::gil_scoped_release release;
 322: 
 323:         py::ssize_t tr_len = len - 1;
 324:         std::vector<double> tr(tr_len);
 325: 
 326:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 327:             double hl = hp[i + 1] - lp[i + 1];
 328:             double hc = std::abs(hp[i + 1] - cp[i]);
 329:             double lc = std::abs(lp[i + 1] - cp[i]);
 330:             tr[i] = std::max({hl, hc, lc});
 331:         }
 332: 
 333:         double init_sum = 0.0;
 334:         for (int i = 0; i < n; ++i) init_sum += tr[i];
 335:         res(n) = init_sum / n;
--- lines 385-475 ---
 385:     for (py::ssize_t i = 0; i < n; ++i) {
 386:         dot += x[i] * y[i];
 387:         norm_x2 += x[i] * x[i];
 388:         norm_y2 += y[i] * y[i];
 389:     }
 390:     double norm_x = std::sqrt(norm_x2);
 391:     double norm_y = std::sqrt(norm_y2);
 392:     if (norm_x < 1e-12 || norm_y < 1e-12) {
 393:         return 0.0;
 394:     }
 395:     return dot / (norm_x * norm_y);
 396: }
 397: 
 398: // 向量版 DTW（兼容旧调用，委托给 span 版）
 399: inline double dtw_distance_vec(const std::vector<double>& x, const std::vector<double>& y, int window = 5) {
 400:     return dtw_distance_span(x.data(), static_cast<py::ssize_t>(x.size()),
 401:                               y.data(), static_cast<py::ssize_t>(y.size()), window);
 402: }
 403: 
 404: // 批量 DTW: 一个 query 对 N 个 candidates（一对一远端循环，GIL 释放）
 405: py::object dtw_distance_batch(
 406:     ArrD query_arr,
 407:     ArrD candidates_arr,
 408:     int window = 5,
 409:     int top_k = 0
 410: ) {
 411:     auto q = query_arr.unchecked<1>();
 412:     auto c = candidates_arr.unchecked<2>();
 413:     py::ssize_t L = q.shape(0);
 414:     py::ssize_t N = c.shape(0);
 415: 
 416:     if (N == 0) {
 417:         if (top_k > 0) {
 418:             ArrI64 empty_idx(0);
 419:             ArrD empty_dist(0);
 420:             return py::make_tuple(empty_idx, empty_dist);
 421:         }
 422:         ArrD empty_result(0);
 423:         return empty_result;
 424:     }
 425: 
 426:     if (c.shape(1) != L) {
 427:         throw std::invalid_argument(
 428:             "candidates.shape[1] must equal query length, got " +
 429:             std::to_string(c.shape(1)) + " vs " + std::to_string(L));
 430:     }
 431: 
 432:     std::vector<double> distances(N);
 433: 
 434:     {
 435:         py::gil_scoped_release release;
 436:         const double* q_ptr = q.data(0);
 437:         for (py::ssize_t i = 0; i < N; ++i) {
 438:             distances[i] = dtw_distance_span(q_ptr, L, c.data(i, 0), L, window);
 439:         }
 440:     }
 441: 
 442:     if (top_k <= 0 || top_k >= static_cast<int>(N)) {
 443:         ArrD result(N);
 444:         auto res_buf = result.mutable_unchecked<1>();
 445:         for (py::ssize_t i = 0; i < N; ++i) res_buf(i) = distances[i];
 446:         return result;
 447:     }
 448: 
 449:     // Top-K via partial_sort
 450:     std::vector<std::pair<double, py::ssize_t>> indexed;
 451:     indexed.reserve(N);
 452:     for (py::ssize_t i = 0; i < N; ++i) {
 453:         indexed.emplace_back(distances[i], i);
 454:     }
 455:     std::partial_sort(
 456:         indexed.begin(),
 457:         indexed.begin() + top_k,
 458:         indexed.end());
 459: 
 460:     ArrI64 top_indices(top_k);
 461:     ArrD top_dists(top_k);
 462:     auto idx_buf = top_indices.mutable_unchecked<1>();
 463:     auto dist_buf = top_dists.mutable_unchecked<1>();
 464:     for (int i = 0; i < top_k; ++i) {
 465:         idx_buf(i) = static_cast<int64_t>(indexed[i].second);
 466:         dist_buf(i) = indexed[i].first;
 467:     }
 468: 
 469:     return py::make_tuple(top_indices, top_dists);
 470: }
 471: 
 472: // 从 Top-K 有效匹配中提取 15 维特征
 473: PatternResult compute_pattern_features_cpp(
 474:     const std::vector<double>& valid_scores,
 475:     const std::vector<double>& valid_frets,
--- lines 475-735 ---
 475:     const std::vector<double>& valid_frets,
 476:     const std::vector<py::ssize_t>& valid_ends,
 477:     int T_back
 478: ) {
 479:     PatternResult r{};
 480:     int top_k_actual = static_cast<int>(valid_scores.size());
 481: 
 482:     // F1-F5: 相似度特征
 483:     r.top1_sim = valid_scores[0];
 484:     int n_avg = std::min(5, top_k_actual);
 485:     double sum_avg = 0.0;
 486:     for (int i = 0; i < n_avg; ++i) sum_avg += valid_scores[i];
 487:     r.top5_avg_sim = sum_avg / n_avg;
 488:     r.sim_decay = r.top1_sim - r.top5_avg_sim;
 489: 
 490:     double var = 0.0, mean_s = 0.0;
 491:     for (auto s : valid_scores) mean_s += s;
 492:     mean_s /= top_k_actual;
 493:     for (auto s : valid_scores) var += (s - mean_s) * (s - mean_s);
 494:     r.sim_variance = (top_k_actual > 1) ? var / top_k_actual : 0.0;
 495:     r.match_distance_ratio = (r.top1_sim > 1e-12) ? r.sim_decay / r.top1_sim : 0.0;
 496: 
 497:     // F6-F11: 后续表现
 498:     double sum_fr = 0.0;
 499:     for (auto fr : valid_frets) sum_fr += fr;
 500:     r.avg_future_ret = sum_fr / top_k_actual;
 501: 
 502:     double sum_ws = 0.0, sum_w = 0.0;
 503:     for (int i = 0; i < top_k_actual; ++i) {
 504:         sum_ws += valid_scores[i] * valid_frets[i];
 505:         sum_w += valid_scores[i];
 506:     }
 507:     r.weighted_future_ret = (sum_w > 1e-12) ? sum_ws / sum_w : r.avg_future_ret;
 508: 
 509:     std::vector<double> sorted_fr = valid_frets;
 510:     std::sort(sorted_fr.begin(), sorted_fr.end());
 511:     r.median_future_ret = (top_k_actual % 2 == 1)
 512:         ? sorted_fr[top_k_actual / 2]
 513:         : (sorted_fr[top_k_actual / 2 - 1] + sorted_fr[top_k_actual / 2]) / 2.0;
 514: 
 515:     int pos_count = 0;
 516:     for (auto fr : valid_frets) if (fr > 0) ++pos_count;
 517:     r.ret_sign_consistency = static_cast<double>(pos_count) / top_k_actual;
 518:     r.best_match_ret = valid_frets[0];
 519: 
 520:     double min_fr = *std::min_element(valid_frets.begin(), valid_frets.end());
 521:     r.max_dd_in_matches = std::max(0.0, -min_fr);
 522: 
 523:     // F12-F15: 匹配质量
 524:     auto [min_e, max_e] = std::minmax_element(valid_ends.begin(), valid_ends.end());
 525:     r.match_time_span = static_cast<double>(*max_e - *min_e);
 526:     r.match_time_span_ratio = r.match_time_span / T_back;
 527: 
 528:     std::vector<py::ssize_t> sorted_ends = valid_ends;
 529:     std::sort(sorted_ends.begin(), sorted_ends.end());
 530:     int max_in_window = 0;
 531:     for (int i = 0; i < top_k_actual; ++i) {
 532:         double target = static_cast<double>(sorted_ends[i]) + 60.0;
 533:         auto it = std::upper_bound(sorted_ends.begin(), sorted_ends.end(),
 534:                                    static_cast<py::ssize_t>(target));
 535:         int count = static_cast<int>(it - sorted_ends.begin()) - i;
 536:         max_in_window = std::max(max_in_window, count);
 537:     }
 538:     r.match_cluster_ratio = static_cast<double>(max_in_window) / top_k_actual;
 539: 
 540:     int above = 0;
 541:     for (auto s : valid_scores) if (s > 0.8) ++above;
 542:     r.n_matches_above_thresh = above;
 543: 
 544:     return r;
 545: }
 546: 
 547: // ═══════════════════════════════════════════════════════════════
 548: // 共享核心：余弦预筛选 → DTW 精排 → 特征提取
 549: // single 和 batch 共用此函数，消除 ~400 行重复逻辑
 550: // ═══════════════════════════════════════════════════════════════
 551: std::optional<PatternResult> pattern_match_core(
 552:     const double* prices, py::ssize_t n_prices,
 553:     int T_idx, int k, int L_query, int T_back,
 554:     int match_step, int M_forward, int dtw_window,
 555:     int cos_prefilter_top,
 556:     const std::vector<double>& query_rets,
 557:     py::ssize_t search_start, py::ssize_t search_end,
 558:     const std::vector<std::vector<double>>* precomputed_rets
 559: ) {
 560:     py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());
 561: 
 562:     // ═══ 第1遍：余弦相似度 + 快速形状距离（全量候选）═══
 563:     std::vector<MatchCandidate> cos_candidates;
 564:     std::vector<double> fast_shape_dists;
 565: 
 566:     for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
 567:         py::ssize_t hist_start = hist_end - L_query + 1;
 568:         if (hist_start < 0) continue;
 569: 
 570:         // 获取标准化收益率：缓存优先，否则现场计算
 571:         const std::vector<double>* hist_rets_ptr = nullptr;
 572:         std::vector<double> hist_rets_scratch;
 573: 
 574:         if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size())) {
 575:             hist_rets_ptr = &(*precomputed_rets)[hist_end];
 576:         } else {
 577:             auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
 578:             if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
 579:                 hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query);
 580:                 hist_rets_ptr = &hist_rets_scratch;
 581:             }
 582:         }
 583: 
 584:         if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;
 585: 
 586:         const auto& hist_rets = *hist_rets_ptr;
 587: 
 588:         // 余弦相似度
 589:         double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
 590:         py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
 591:         for (py::ssize_t i = 0; i < min_len; ++i) {
 592:             dot += hist_rets[i] * query_rets[i];
 593:             nx2 += hist_rets[i] * hist_rets[i];
 594:             ny2 += query_rets[i] * query_rets[i];
 595:         }
 596:         double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
 597:         double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;
 598: 
 599:         // 快速形状距离
 600:         double fast_d2 = 0.0;
 601:         for (py::ssize_t i = 0; i < min_len; ++i) {
 602:             double diff = hist_rets[i] - query_rets[i];
 603:             fast_d2 += diff * diff;
 604:         }
 605:         fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));
 606: 
 607:         if (cos_s > 0) {
 608:             cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
 609:         }
 610:     }
 611: 
 612:     if (cos_candidates.size() < 3) return std::nullopt;
 613: 
 614:     // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
 615:     double sigma_fast = 1.0;
 616:     if (fast_shape_dists.size() > 1) {
 617:         double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0.0)
 618:                         / fast_shape_dists.size();
 619:         double var_fd = 0.0;
 620:         for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
 621:         var_fd /= fast_shape_dists.size();
 622:         sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)));
 623:     }
 624:     sigma_fast = std::max(sigma_fast, 1e-12);
 625: 
 626:     // 余弦排序 + 全量边界
 627:     std::sort(cos_candidates.begin(), cos_candidates.end(),
 628:               [](const MatchCandidate& a, const MatchCandidate& b) { return a.cos_s > b.cos_s; });
 629: 
 630:     double global_min_cos = cos_candidates.back().cos_s;
 631:     double global_max_cos = cos_candidates.front().cos_s;
 632: 
 633:     int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
 634:     cos_candidates.resize(n_cos);
 635: 
 636:     // ═══ 第2遍：DTW 精排 (仅 top-N) ═══
 637:     std::vector<double> dtw_dists, cos_sims, future_rets;
 638:     std::vector<py::ssize_t> match_ends;
 639:     dtw_dists.reserve(n_cos);
 640:     cos_sims.reserve(n_cos);
 641:     future_rets.reserve(n_cos);
 642:     match_ends.reserve(n_cos);
 643: 
 644:     for (const auto& cand : cos_candidates) {
 645:         py::ssize_t hn = static_cast<py::ssize_t>(cand.hist_rets.size());
 646:         double dtw_d = dtw_distance_span(cand.hist_rets.data(), hn,
 647:                                           query_rets.data(), n_query, dtw_window);
 648: 
 649:         dtw_dists.push_back(dtw_d);
 650:         cos_sims.push_back(cand.cos_s);
 651: 
 652:         py::ssize_t fut_end = cand.hist_end + M_forward;
 653:         if (fut_end < n_prices && fut_end < T_idx) {
 654:             future_rets.push_back(prices[fut_end] / prices[cand.hist_end] - 1.0);
 655:         } else {
 656:             future_rets.push_back(std::numeric_limits<double>::quiet_NaN());
 657:         }
 658:         match_ends.push_back(cand.hist_end);
 659:     }
 660: 
 661:     if (dtw_dists.size() < 3) return std::nullopt;
 662: 
 663:     // sim_dtw = exp(-dtw/sigma)
 664:     double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;
 665: 
 666:     std::vector<double> sim_dtw(dtw_dists.size());
 667:     double min_dtw_v = std::numeric_limits<double>::max();
 668:     double max_dtw_v = std::numeric_limits<double>::lowest();
 669:     for (size_t i = 0; i < dtw_dists.size(); ++i) {
 670:         sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
 671:         min_dtw_v = std::min(min_dtw_v, sim_dtw[i]);
 672:         max_dtw_v = std::max(max_dtw_v, sim_dtw[i]);
 673:     }
 674: 
 675:     // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
 676:     double range_dtw = (max_dtw_v - min_dtw_v > 1e-12) ? (max_dtw_v - min_dtw_v) : 1.0;
 677:     double range_cos_val = (global_max_cos - global_min_cos > 1e-12)
 678:                            ? (global_max_cos - global_min_cos) : 1.0;
 679: 
 680:     struct Scored { double score, fut_ret; py::ssize_t end_idx; };
 681:     std::vector<Scored> scored;
 682:     scored.reserve(sim_dtw.size());
 683:     for (size_t i = 0; i < sim_dtw.size(); ++i) {
 684:         double nd = (sim_dtw[i] - min_dtw_v) / range_dtw;
 685:         double nc = (cos_sims[i] - global_min_cos) / range_cos_val;
 686:         scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
 687:     }
 688: 
 689:     std::sort(scored.begin(), scored.end(),
 690:               [](const Scored& a, const Scored& b) { return a.score > b.score; });
 691: 
 692:     int top_k = std::min(k, static_cast<int>(scored.size()));
 693: 
 694:     // 过滤 NaN 未来收益
 695:     std::vector<double> valid_scores, valid_frets;
 696:     std::vector<py::ssize_t> valid_ends;
 697:     for (int i = 0; i < top_k; ++i) {
 698:         if (!std::isnan(scored[i].fut_ret)) {
 699:             valid_scores.push_back(scored[i].score);
 700:             valid_frets.push_back(scored[i].fut_ret);
 701:             valid_ends.push_back(scored[i].end_idx);
 702:         }
 703:     }
 704:     if (valid_scores.size() < 2) return std::nullopt;
 705: 
 706:     return compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);
 707: }
 708: 
 709: } // namespace
 710: 
 711: // ═══════════════════════════════════════════════════════════════
 712: // 第六部分-A: 单点形态匹配（薄包装 → pattern_match_core）
 713: // ═══════════════════════════════════════════════════════════════
 714: py::object pattern_match_single(
 715:     ArrD prices_arr,
 716:     int T_idx,
 717:     int k = 10,
 718:     int L_query = 20,
 719:     int T_back = 750,
 720:     int match_step = 1,
 721:     int M_forward = 5,
 722:     int dtw_window = 5,
 723:     int cos_prefilter_top = 50
 724: ) {
 725:     auto prices_buf = prices_arr.unchecked<1>();
 726:     py::ssize_t n_prices = prices_buf.shape(0);
 727:     const double* prices = prices_buf.data(0);
 728: 
 729:     // ── 输入校验 ──
 730:     if (T_idx < 0 || static_cast<py::ssize_t>(T_idx) >= n_prices) {
 731:         throw std::out_of_range("T_idx must satisfy 0 <= T_idx < len(prices), got " + std::to_string(T_idx));
 732:     }
 733:     if (L_query < 3) {
 734:         throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
 735:     }
--- lines 735-910 ---
 735:     }
 736:     if (T_back <= 0) {
 737:         throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
 738:     }
 739:     if (k <= 0) {
 740:         throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
 741:     }
 742:     if (M_forward < 1) {
 743:         throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
 744:     }
 745:     if (match_step <= 0) {
 746:         throw std::invalid_argument("match_step must be > 0");
 747:     }
 748:     if (dtw_window < 0) {
 749:         throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
 750:     }
 751:     if (cos_prefilter_top <= 0) {
 752:         throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
 753:     }
 754:     if (T_idx < L_query + M_forward + 10) return py::none();
 755:     if (T_idx - L_query + 1 < 0) return py::none();
 756: 
 757:     // 查询窗口标准化
 758:     auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
 759:     if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) return py::none();
 760: 
 761:     std::vector<double> query_rets;
 762:     {
 763:         py::gil_scoped_release release;
 764:         query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
 765:     }
 766:     if (query_rets.size() < 2) return py::none();
 767: 
 768:     py::ssize_t search_end = T_idx - L_query;
 769:     if (search_end < L_query) return py::none();
 770:     py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
 771:                                         py::ssize_t(T_idx - T_back));
 772: 
 773:     // ── 委托共享核心（无预计算缓存，现场标准化）──
 774:     std::optional<PatternResult> result_opt;
 775:     {
 776:         py::gil_scoped_release release;
 777:         result_opt = pattern_match_core(
 778:             prices, n_prices, T_idx, k, L_query, T_back,
 779:             match_step, M_forward, dtw_window, cos_prefilter_top,
 780:             query_rets, search_start, search_end,
 781:             nullptr  // 无预计算缓存
 782:         );
 783:     }
 784: 
 785:     if (!result_opt.has_value()) return py::none();
 786: 
 787:     // ── 构造返回值 ──
 788:     py::dict result;
 789:     result["top1_sim"] = result_opt->top1_sim;
 790:     result["top5_avg_sim"] = result_opt->top5_avg_sim;
 791:     result["sim_decay"] = result_opt->sim_decay;
 792:     result["sim_variance"] = result_opt->sim_variance;
 793:     result["match_distance_ratio"] = result_opt->match_distance_ratio;
 794:     result["avg_future_ret"] = result_opt->avg_future_ret;
 795:     result["weighted_future_ret"] = result_opt->weighted_future_ret;
 796:     result["median_future_ret"] = result_opt->median_future_ret;
 797:     result["ret_sign_consistency"] = result_opt->ret_sign_consistency;
 798:     result["best_match_ret"] = result_opt->best_match_ret;
 799:     result["max_dd_in_matches"] = result_opt->max_dd_in_matches;
 800:     result["match_time_span"] = result_opt->match_time_span;
 801:     result["match_time_span_ratio"] = result_opt->match_time_span_ratio;
 802:     result["match_cluster_ratio"] = result_opt->match_cluster_ratio;
 803:     result["n_matches_above_thresh"] = result_opt->n_matches_above_thresh;
 804:     return result;
 805: }
 806: 
 807: // ═══════════════════════════════════════════════════════════════
 808: // 第七部分: 批量形态匹配 (v3 新增)
 809: // ═══════════════════════════════════════════════════════════════
 810: 
 811: py::tuple pattern_match_batch(
 812:     ArrD prices_arr,
 813:     ArrI64 t_indices_arr,
 814:     int k = 10,
 815:     int L_query = 20,
 816:     int T_back = 750,
 817:     int match_step = 1,
 818:     int M_forward = 5,
 819:     int dtw_window = 5,
 820:     int cos_prefilter_top = 50
 821: ) {
 822:     auto prices_buf = prices_arr.unchecked<1>();
 823:     py::ssize_t n_prices = prices_buf.shape(0);
 824:     const double* prices = prices_buf.data(0);
 825: 
 826:     auto t_buf = t_indices_arr.unchecked<1>();
 827:     py::ssize_t n_samples = t_buf.shape(0);
 828:     const int64_t* t_ptr = t_buf.data(0);
 829: 
 830:     // ── 输入校验 ──
 831:     if (L_query < 3) {
 832:         throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
 833:     }
 834:     if (T_back <= 0) {
 835:         throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
 836:     }
 837:     if (k <= 0) {
 838:         throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
 839:     }
 840:     if (M_forward < 1) {
 841:         throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
 842:     }
 843:     if (match_step <= 0) {
 844:         throw std::invalid_argument("match_step must be > 0");
 845:     }
 846:     if (dtw_window < 0) {
 847:         throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
 848:     }
 849:     if (cos_prefilter_top <= 0) {
 850:         throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
 851:     }
 852:     if (n_samples == 0) {
 853:         ArrD empty_features(std::vector<py::ssize_t>{0, 15});
 854:         py::array_t<bool> empty_mask(std::vector<py::ssize_t>{0});
 855:         return py::make_tuple(empty_features, empty_mask);
 856:     }
 857: 
 858:     for (py::ssize_t i = 1; i < n_samples; ++i) {
 859:         if (t_ptr[i] <= t_ptr[i - 1]) {
 860:             throw std::invalid_argument("t_indices must be strictly increasing");
 861:         }
 862:     }
 863:     if (t_ptr[n_samples - 1] >= n_prices) {
 864:         throw std::invalid_argument("max(t_indices) must be < len(prices)");
 865:     }
 866: 
 867:     std::vector<double> features_flat;
 868:     features_flat.reserve(n_samples * 15);
 869:     std::vector<bool> valid_mask(n_samples, false);
 870: 
 871:     {
 872:         // ── GIL 释放区：纯 C++ 批量计算 ──
 873:         py::gil_scoped_release release;
 874: 
 875:         // ── 第一遍：计算所有 T_idx 搜索范围的并集（避免预计算无用窗口）──
 876:         py::ssize_t precompute_start = n_prices;
 877:         py::ssize_t precompute_end = 0;
 878:         for (py::ssize_t s = 0; s < n_samples; ++s) {
 879:             int T_idx = static_cast<int>(t_ptr[s]);
 880:             if (T_idx < L_query + M_forward + 10) continue;
 881:             py::ssize_t s_end = T_idx - L_query;
 882:             if (s_end < L_query) continue;
 883:             py::ssize_t s_start = std::max(py::ssize_t(L_query - 1),
 884:                                            py::ssize_t(T_idx - T_back));
 885:             if (s_start < s_end) {
 886:                 precompute_start = std::min(precompute_start, s_start);
 887:                 precompute_end = std::max(precompute_end, s_end);
 888:             }
 889:         }
 890: 
 891:         // ── 仅预计算搜索范围并集内的窗口标准化收益率 ──
 892:         std::vector<std::vector<double>> precomputed_rets(n_prices);
 893:         if (precompute_start <= precompute_end) {
 894:             for (py::ssize_t end = precompute_start; end <= precompute_end; ++end) {
 895:                 py::ssize_t start = end - L_query + 1;
 896:                 if (start >= 0) {
 897:                     auto window_prices = extract_window(prices, start, end);
 898:                     precomputed_rets[end] = standardize_returns_cpp(window_prices.data(), L_query);
 899:                 }
 900:             }
 901:         }
 902: 
 903:         // ── 对每个 T_idx 执行形态匹配（复用预计算缓存）──
 904:         for (py::ssize_t s = 0; s < n_samples; ++s) {
 905:             int T_idx = static_cast<int>(t_ptr[s]);
 906: 
 907:             if (T_idx < L_query + M_forward + 10) continue;
 908:             if (T_idx - L_query + 1 < 0) continue;
 909: 
 910:             auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 '"'src/cpp/etf_core.cpp'; for ("'$i=45; $i -le 335; $i++) { '"'{0,4}: {1}' -f "'$i, $lines[$i-1] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 193ms:
  45: #include <algorithm>
  46: #include <limits>
  47: #include <numeric>
  48: #include <optional>
  49: #include <stdexcept>
  50: 
  51: namespace py = pybind11;
  52: 
  53: // ── 类型别名 (v2: forcecast 策略) ──
  54: using ArrD  = py::array_t<double, py::array::c_style | py::array::forcecast>;
  55: using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;
  56: 
  57: // ═══════════════════════════════════════════════════════════════
  58: // 第一部分: 序列标准化 (V3.3.py 行 362-373)
  59: // ═══════════════════════════════════════════════════════════════
  60: 
  61: std::vector<double> standardize_returns_cpp(const double* prices, py::ssize_t n) {
  62:     if (n < 2) {
  63:         return {};  // 返回空向量表示无效窗口
  64:     }
  65: 
  66:     // 窗口级检查：任一价格为非有限值 → 整个窗口无效
  67:     for (py::ssize_t i = 0; i < n; ++i) {
  68:         if (!std::isfinite(prices[i])) {
  69:             return {};
  70:         }
  71:     }
  72: 
  73:     // 计算对数收益率（所有价格已通过有限性检查，长度固定为 n-1）
  74:     std::vector<double> rets;
  75:     rets.reserve(n - 1);
  76:     for (py::ssize_t i = 1; i < n; ++i) {
  77:         double p_prev = std::max(prices[i - 1], 1e-12);
  78:         double p_curr = std::max(prices[i], 1e-12);
  79:         rets.push_back(std::log(p_curr / p_prev));
  80:     }
  81: 
  82:     if (rets.empty()) {
  83:         return {};
  84:     }
  85: 
  86:     // 去均值
  87:     double mean = std::accumulate(rets.begin(), rets.end(), 0.0) / rets.size();
  88:     for (auto& r : rets) r -= mean;
  89: 
  90:     // 标准差
  91:     double sq_sum = 0.0;
  92:     for (auto r : rets) sq_sum += r * r;
  93:     double std_val = std::sqrt(sq_sum / rets.size());
  94: 
  95:     if (std_val < 1e-12) {
  96:         return rets;  // 已去均值，不再除以 std
  97:     }
  98: 
  99:     for (auto& r : rets) r /= std_val;
 100:     return rets;
 101: }
 102: 
 103: // Python 绑定包装
 104: ArrD standardize_returns(ArrD price_series) {
 105:     auto buf = price_series.unchecked<1>();
 106:     py::ssize_t n = buf.shape(0);
 107:     const double* ptr = buf.data(0);
 108: 
 109:     std::vector<double> result_vec;
 110:     {
 111:         py::gil_scoped_release release;
 112:         result_vec = standardize_returns_cpp(ptr, n);
 113:     }
 114: 
 115:     py::ssize_t m = static_cast<py::ssize_t>(result_vec.size());
 116:     ArrD result(m);
 117:     auto res_buf = result.mutable_unchecked<1>();
 118:     for (py::ssize_t i = 0; i < m; ++i) {
 119:         res_buf(i) = result_vec[i];
 120:     }
 121:     return result;
 122: }
 123: 
 124: // ═══════════════════════════════════════════════════════════════
 125: // 第二部分: 余弦相似度 (V3.3.py 行 376-382)
 126: // ═══════════════════════════════════════════════════════════════
 127: 
 128: double cosine_similarity(ArrD x_arr, ArrD y_arr) {
 129:     auto x = x_arr.unchecked<1>();
 130:     auto y = y_arr.unchecked<1>();
 131:     py::ssize_t n = x.shape(0);
 132: 
 133:     if (n != y.shape(0)) {
 134:         throw std::invalid_argument("x and y must have same length");
 135:     }
 136: 
 137:     const double* xp = x.data(0);
 138:     const double* yp = y.data(0);
 139: 
 140:     double dot, norm_x2, norm_y2;
 141:     {
 142:         py::gil_scoped_release release;
 143:         dot = 0.0; norm_x2 = 0.0; norm_y2 = 0.0;
 144:         for (py::ssize_t i = 0; i < n; ++i) {
 145:             dot += xp[i] * yp[i];
 146:             norm_x2 += xp[i] * xp[i];
 147:             norm_y2 += yp[i] * yp[i];
 148:         }
 149:     }
 150: 
 151:     double norm_x = std::sqrt(norm_x2);
 152:     double norm_y = std::sqrt(norm_y2);
 153:     if (norm_x < 1e-12 || norm_y < 1e-12) {
 154:         return 0.0;
 155:     }
 156:     return dot / (norm_x * norm_y);
 157: }
 158: 
 159: // ═══════════════════════════════════════════════════════════════
 160: // 第三部分: DTW 距离 (V3.3.py 行 339-359)
 161: // ═══════════════════════════════════════════════════════════════
 162: 
 163: // Span版 DTW 距离（零拷贝 + 滚动双行数组，O(m) 内存）
 164: // 供 public API 和内部批量函数共用
 165: double dtw_distance_span(const double* x, py::ssize_t n,
 166:                           const double* y, py::ssize_t m,
 167:                           int window = 5) {
 168:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 169: 
 170:     int band = std::max(window, static_cast<int>(std::abs(n - m)));
 171:     const double INF = std::numeric_limits<double>::infinity();
 172: 
 173:     std::vector<double> prev(m + 1, INF);
 174:     std::vector<double> curr(m + 1, INF);
 175:     prev[0] = 0.0;
 176: 
 177:     for (py::ssize_t i = 1; i <= n; ++i) {
 178:         py::ssize_t j_start = std::max(py::ssize_t(1), i - band);
 179:         py::ssize_t j_end = std::min(m, i + band);
 180: 
 181:         for (py::ssize_t j = j_start; j <= j_end; ++j) {
 182:             double cost = x[i - 1] - y[j - 1];
 183:             cost *= cost;
 184: 
 185:             double pj = (std::abs((i - 1) - j) <= band) ? prev[j] : INF;
 186:             double cj = (j > j_start) ? curr[j - 1] : INF;
 187:             double pj1 = prev[j - 1];
 188: 
 189:             curr[j] = cost + std::min({pj, cj, pj1});
 190:         }
 191: 
 192:         std::swap(prev, curr);
 193:         // dtw[i][0] = INF for all i > 0（prev[0] 经 swap 可能残留 0.0）
 194:         prev[0] = INF;
 195:     }
 196: 
 197:     double path_len = static_cast<double>(n + m);
 198:     return (path_len > 0) ? std::sqrt(prev[m]) / path_len : INF;
 199: }
 200: 
 201: double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
 202:     auto x = x_arr.unchecked<1>();
 203:     auto y = y_arr.unchecked<1>();
 204:     py::ssize_t n = x.shape(0);
 205:     py::ssize_t m = y.shape(0);
 206: 
 207:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 208: 
 209:     double result;
 210:     {
 211:         py::gil_scoped_release release;
 212:         result = dtw_distance_span(x.data(0), n, y.data(0), m, window);
 213:     }
 214: 
 215:     return result;
 216: }
 217: 
 218: // ═══════════════════════════════════════════════════════════════
 219: // 第四部分: ADX 计算 (V3.3.py 行 757-795)
 220: // ═══════════════════════════════════════════════════════════════
 221: 
 222: double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 223:     if (n <= 0) {
 224:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 225:     }
 226:     auto high = high_arr.unchecked<1>();
 227:     auto low  = low_arr.unchecked<1>();
 228:     auto close = close_arr.unchecked<1>();
 229:     py::ssize_t len = high.shape(0);
 230: 
 231:     if (len < n + 16) return 25.0;
 232:     if (low.shape(0) != len || close.shape(0) != len) {
 233:         throw std::invalid_argument("high/low/close must have same length");
 234:     }
 235: 
 236:     double result;
 237:     {
 238:         py::gil_scoped_release release;
 239: 
 240:         py::ssize_t tr_len = len - 1;
 241:         std::vector<double> tr(tr_len), plus_dm(tr_len), minus_dm(tr_len);
 242: 
 243:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 244:             double hl = high(i + 1) - low(i + 1);
 245:             double hc = std::abs(high(i + 1) - close(i));
 246:             double lc = std::abs(low(i + 1) - close(i));
 247:             tr[i] = std::max({hl, hc, lc});
 248: 
 249:             double up = high(i + 1) - high(i);
 250:             double down = low(i) - low(i + 1);
 251:             plus_dm[i]  = (up > down && up > 0) ? up : 0.0;
 252:             minus_dm[i] = (down > up && down > 0) ? down : 0.0;
 253:         }
 254: 
 255:         // Wilder's smoothing
 256:         auto wilder_smooth = [&](const std::vector<double>& raw) {
 257:             std::vector<double> smoothed(tr_len, 0.0);
 258:             double init_sum = 0.0;
 259:             for (int i = 0; i < n; ++i) init_sum += raw[i];
 260:             // Fill first n positions with initial mean (match Python behaviour)
 261:             double init_mean = init_sum / n;
 262:             for (int i = 0; i < n; ++i) smoothed[i] = init_mean;
 263:             for (py::ssize_t i = n; i < tr_len; ++i) {
 264:                 smoothed[i] = (smoothed[i - 1] * (n - 1) + raw[i]) / n;
 265:             }
 266:             return smoothed;
 267:         };
 268: 
 269:         auto atr_s = wilder_smooth(tr);
 270:         auto plus_s = wilder_smooth(plus_dm);
 271:         auto minus_s = wilder_smooth(minus_dm);
 272: 
 273:         std::vector<double> dx(tr_len);
 274:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 275:             double pdi = 100.0 * plus_s[i] / (atr_s[i] + 1e-12);
 276:             double mdi = 100.0 * minus_s[i] / (atr_s[i] + 1e-12);
 277:             dx[i] = 100.0 * std::abs(pdi - mdi) / (pdi + mdi + 1e-12);
 278:         }
 279: 
 280:         auto adx_s = wilder_smooth(dx);
 281:         result = adx_s.back();
 282:     }
 283: 
 284:     return result;
 285: }
 286: 
 287: // ═══════════════════════════════════════════════════════════════
 288: // 第五部分: ATR 计算
 289: // ═══════════════════════════════════════════════════════════════
 290: 
 291: ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 292:     if (n <= 0) {
 293:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 294:     }
 295:     auto high = high_arr.unchecked<1>();
 296:     auto low  = low_arr.unchecked<1>();
 297:     auto close = close_arr.unchecked<1>();
 298:     py::ssize_t len = high.shape(0);
 299: 
 300:     // v3: 输入校验 (GPT-5.5 最终审查 P0)
 301:     if (low.shape(0) != len || close.shape(0) != len) {
 302:         throw std::invalid_argument("high/low/close must have same length");
 303:     }
 304:     if (len < n + 1) {
 305:         ArrD result(len);
 306:         auto res = result.mutable_unchecked<1>();
 307:         for (py::ssize_t i = 0; i < len; ++i)
 308:             res(i) = std::numeric_limits<double>::quiet_NaN();
 309:         return result;
 310:     }
 311: 
 312:     const double* hp = high.data(0);
 313:     const double* lp = low.data(0);
 314:     const double* cp = close.data(0);
 315: 
 316:     ArrD result(len);
 317:     auto res = result.mutable_unchecked<1>();
 318:     for (py::ssize_t i = 0; i < n; ++i) res(i) = std::numeric_limits<double>::quiet_NaN();
 319: 
 320:     {
 321:         py::gil_scoped_release release;
 322: 
 323:         py::ssize_t tr_len = len - 1;
 324:         std::vector<double> tr(tr_len);
 325: 
 326:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 327:             double hl = hp[i + 1] - lp[i + 1];
 328:             double hc = std::abs(hp[i + 1] - cp[i]);
 329:             double lc = std::abs(lp[i + 1] - cp[i]);
 330:             tr[i] = std::max({hl, hc, lc});
 331:         }
 332: 
 333:         double init_sum = 0.0;
 334:         for (int i = 0; i < n; ++i) init_sum += tr[i];
 335:         res(n) = init_sum / n;

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 '"'src/cpp/etf_core.cpp'; foreach ("'$range in @(@(160,225), @(291,355), @(385,470))) { $start=$range[0]; $end=$range[1]; Write-Output "--- lines $start-$end ---"; for ($i=$start; $i -le $end; $i++) { '"'{0,4}: {1}' -f "'$i, $lines[$i-1] } }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 198ms:
--- lines 160-225 ---
 160: // 第三部分: DTW 距离 (V3.3.py 行 339-359)
 161: // ═══════════════════════════════════════════════════════════════
 162: 
 163: // Span版 DTW 距离（零拷贝 + 滚动双行数组，O(m) 内存）
 164: // 供 public API 和内部批量函数共用
 165: double dtw_distance_span(const double* x, py::ssize_t n,
 166:                           const double* y, py::ssize_t m,
 167:                           int window = 5) {
 168:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 169: 
 170:     int band = std::max(window, static_cast<int>(std::abs(n - m)));
 171:     const double INF = std::numeric_limits<double>::infinity();
 172: 
 173:     std::vector<double> prev(m + 1, INF);
 174:     std::vector<double> curr(m + 1, INF);
 175:     prev[0] = 0.0;
 176: 
 177:     for (py::ssize_t i = 1; i <= n; ++i) {
 178:         py::ssize_t j_start = std::max(py::ssize_t(1), i - band);
 179:         py::ssize_t j_end = std::min(m, i + band);
 180: 
 181:         for (py::ssize_t j = j_start; j <= j_end; ++j) {
 182:             double cost = x[i - 1] - y[j - 1];
 183:             cost *= cost;
 184: 
 185:             double pj = (std::abs((i - 1) - j) <= band) ? prev[j] : INF;
 186:             double cj = (j > j_start) ? curr[j - 1] : INF;
 187:             double pj1 = prev[j - 1];
 188: 
 189:             curr[j] = cost + std::min({pj, cj, pj1});
 190:         }
 191: 
 192:         std::swap(prev, curr);
 193:         // dtw[i][0] = INF for all i > 0（prev[0] 经 swap 可能残留 0.0）
 194:         prev[0] = INF;
 195:     }
 196: 
 197:     double path_len = static_cast<double>(n + m);
 198:     return (path_len > 0) ? std::sqrt(prev[m]) / path_len : INF;
 199: }
 200: 
 201: double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
 202:     auto x = x_arr.unchecked<1>();
 203:     auto y = y_arr.unchecked<1>();
 204:     py::ssize_t n = x.shape(0);
 205:     py::ssize_t m = y.shape(0);
 206: 
 207:     if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();
 208: 
 209:     double result;
 210:     {
 211:         py::gil_scoped_release release;
 212:         result = dtw_distance_span(x.data(0), n, y.data(0), m, window);
 213:     }
 214: 
 215:     return result;
 216: }
 217: 
 218: // ═══════════════════════════════════════════════════════════════
 219: // 第四部分: ADX 计算 (V3.3.py 行 757-795)
 220: // ═══════════════════════════════════════════════════════════════
 221: 
 222: double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 223:     if (n <= 0) {
 224:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 225:     }
--- lines 291-355 ---
 291: ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
 292:     if (n <= 0) {
 293:         throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
 294:     }
 295:     auto high = high_arr.unchecked<1>();
 296:     auto low  = low_arr.unchecked<1>();
 297:     auto close = close_arr.unchecked<1>();
 298:     py::ssize_t len = high.shape(0);
 299: 
 300:     // v3: 输入校验 (GPT-5.5 最终审查 P0)
 301:     if (low.shape(0) != len || close.shape(0) != len) {
 302:         throw std::invalid_argument("high/low/close must have same length");
 303:     }
 304:     if (len < n + 1) {
 305:         ArrD result(len);
 306:         auto res = result.mutable_unchecked<1>();
 307:         for (py::ssize_t i = 0; i < len; ++i)
 308:             res(i) = std::numeric_limits<double>::quiet_NaN();
 309:         return result;
 310:     }
 311: 
 312:     const double* hp = high.data(0);
 313:     const double* lp = low.data(0);
 314:     const double* cp = close.data(0);
 315: 
 316:     ArrD result(len);
 317:     auto res = result.mutable_unchecked<1>();
 318:     for (py::ssize_t i = 0; i < n; ++i) res(i) = std::numeric_limits<double>::quiet_NaN();
 319: 
 320:     {
 321:         py::gil_scoped_release release;
 322: 
 323:         py::ssize_t tr_len = len - 1;
 324:         std::vector<double> tr(tr_len);
 325: 
 326:         for (py::ssize_t i = 0; i < tr_len; ++i) {
 327:             double hl = hp[i + 1] - lp[i + 1];
 328:             double hc = std::abs(hp[i + 1] - cp[i]);
 329:             double lc = std::abs(lp[i + 1] - cp[i]);
 330:             tr[i] = std::max({hl, hc, lc});
 331:         }
 332: 
 333:         double init_sum = 0.0;
 334:         for (int i = 0; i < n; ++i) init_sum += tr[i];
 335:         res(n) = init_sum / n;
 336: 
 337:         for (py::ssize_t i = n + 1; i < len; ++i) {
 338:             res(i) = (res(i - 1) * (n - 1) + tr[i - 1]) / n;
 339:         }
 340:     }
 341:     return result;
 342: }
 343: 
 344: // ═══════════════════════════════════════════════════════════════
 345: // 第六部分: 形态匹配引擎 (V3.3.py 行 389-627)
 346: // ═══════════════════════════════════════════════════════════════
 347: 
 348: namespace {
 349: 
 350: struct MatchCandidate {
 351:     py::ssize_t hist_end;
 352:     py::ssize_t hist_start;
 353:     double cos_s;
 354:     std::vector<double> hist_rets;
 355: };
--- lines 385-470 ---
 385:     for (py::ssize_t i = 0; i < n; ++i) {
 386:         dot += x[i] * y[i];
 387:         norm_x2 += x[i] * x[i];
 388:         norm_y2 += y[i] * y[i];
 389:     }
 390:     double norm_x = std::sqrt(norm_x2);
 391:     double norm_y = std::sqrt(norm_y2);
 392:     if (norm_x < 1e-12 || norm_y < 1e-12) {
 393:         return 0.0;
 394:     }
 395:     return dot / (norm_x * norm_y);
 396: }
 397: 
 398: // 向量版 DTW（兼容旧调用，委托给 span 版）
 399: inline double dtw_distance_vec(const std::vector<double>& x, const std::vector<double>& y, int window = 5) {
 400:     return dtw_distance_span(x.data(), static_cast<py::ssize_t>(x.size()),
 401:                               y.data(), static_cast<py::ssize_t>(y.size()), window);
 402: }
 403: 
 404: // 批量 DTW: 一个 query 对 N 个 candidates（一对一远端循环，GIL 释放）
 405: py::object dtw_distance_batch(
 406:     ArrD query_arr,
 407:     ArrD candidates_arr,
 408:     int window = 5,
 409:     int top_k = 0
 410: ) {
 411:     auto q = query_arr.unchecked<1>();
 412:     auto c = candidates_arr.unchecked<2>();
 413:     py::ssize_t L = q.shape(0);
 414:     py::ssize_t N = c.shape(0);
 415: 
 416:     if (N == 0) {
 417:         if (top_k > 0) {
 418:             ArrI64 empty_idx(0);
 419:             ArrD empty_dist(0);
 420:             return py::make_tuple(empty_idx, empty_dist);
 421:         }
 422:         ArrD empty_result(0);
 423:         return empty_result;
 424:     }
 425: 
 426:     if (c.shape(1) != L) {
 427:         throw std::invalid_argument(
 428:             "candidates.shape[1] must equal query length, got " +
 429:             std::to_string(c.shape(1)) + " vs " + std::to_string(L));
 430:     }
 431: 
 432:     std::vector<double> distances(N);
 433: 
 434:     {
 435:         py::gil_scoped_release release;
 436:         const double* q_ptr = q.data(0);
 437:         for (py::ssize_t i = 0; i < N; ++i) {
 438:             distances[i] = dtw_distance_span(q_ptr, L, c.data(i, 0), L, window);
 439:         }
 440:     }
 441: 
 442:     if (top_k <= 0 || top_k >= static_cast<int>(N)) {
 443:         ArrD result(N);
 444:         auto res_buf = result.mutable_unchecked<1>();
 445:         for (py::ssize_t i = 0; i < N; ++i) res_buf(i) = distances[i];
 446:         return result;
 447:     }
 448: 
 449:     // Top-K via partial_sort
 450:     std::vector<std::pair<double, py::ssize_t>> indexed;
 451:     indexed.reserve(N);
 452:     for (py::ssize_t i = 0; i < N; ++i) {
 453:         indexed.emplace_back(distances[i], i);
 454:     }
 455:     std::partial_sort(
 456:         indexed.begin(),
 457:         indexed.begin() + top_k,
 458:         indexed.end());
 459: 
 460:     ArrI64 top_indices(top_k);
 461:     ArrD top_dists(top_k);
 462:     auto idx_buf = top_indices.mutable_unchecked<1>();
 463:     auto dist_buf = top_dists.mutable_unchecked<1>();
 464:     for (int i = 0; i < top_k; ++i) {
 465:         idx_buf(i) = static_cast<int64_t>(indexed[i].second);
 466:         dist_buf(i) = indexed[i].first;
 467:     }
 468: 
 469:     return py::make_tuple(top_indices, top_dists);
 470: }

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 '"'src/cpp/etf_core.cpp'; for ("'$i=345; $i -le 810; $i++) { '"'{0,4}: {1}' -f "'$i, $lines[$i-1] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 185ms:
 345: // 第六部分: 形态匹配引擎 (V3.3.py 行 389-627)
 346: // ═══════════════════════════════════════════════════════════════
 347: 
 348: namespace {
 349: 
 350: struct MatchCandidate {
 351:     py::ssize_t hist_end;
 352:     py::ssize_t hist_start;
 353:     double cos_s;
 354:     std::vector<double> hist_rets;
 355: };
 356: 
 357: struct PatternResult {
 358:     double top1_sim, top5_avg_sim, sim_decay, sim_variance;
 359:     double match_distance_ratio, avg_future_ret, weighted_future_ret;
 360:     double median_future_ret, ret_sign_consistency, best_match_ret;
 361:     double max_dd_in_matches, match_time_span, match_time_span_ratio;
 362:     double match_cluster_ratio;
 363:     int n_matches_above_thresh;
 364: };
 365: 
 366: // 从价格数组提取窗口
 367: std::vector<double> extract_window(const double* prices, py::ssize_t start, py::ssize_t end) {
 368:     std::vector<double> result;
 369:     result.reserve(end - start + 1);
 370:     for (py::ssize_t i = start; i <= end; ++i) {
 371:         result.push_back(prices[i]);
 372:     }
 373:     return result;
 374: }
 375: 
 376: // 向量版余弦相似度（用于批量内部计算）
 377: double cosine_similarity_vec(const std::vector<double>& x, const std::vector<double>& y) {
 378:     py::ssize_t n = static_cast<py::ssize_t>(x.size());
 379:     if (n != static_cast<py::ssize_t>(y.size())) {
 380:         return 0.0;
 381:     }
 382:     if (n == 0) return 0.0;
 383: 
 384:     double dot = 0.0, norm_x2 = 0.0, norm_y2 = 0.0;
 385:     for (py::ssize_t i = 0; i < n; ++i) {
 386:         dot += x[i] * y[i];
 387:         norm_x2 += x[i] * x[i];
 388:         norm_y2 += y[i] * y[i];
 389:     }
 390:     double norm_x = std::sqrt(norm_x2);
 391:     double norm_y = std::sqrt(norm_y2);
 392:     if (norm_x < 1e-12 || norm_y < 1e-12) {
 393:         return 0.0;
 394:     }
 395:     return dot / (norm_x * norm_y);
 396: }
 397: 
 398: // 向量版 DTW（兼容旧调用，委托给 span 版）
 399: inline double dtw_distance_vec(const std::vector<double>& x, const std::vector<double>& y, int window = 5) {
 400:     return dtw_distance_span(x.data(), static_cast<py::ssize_t>(x.size()),
 401:                               y.data(), static_cast<py::ssize_t>(y.size()), window);
 402: }
 403: 
 404: // 批量 DTW: 一个 query 对 N 个 candidates（一对一远端循环，GIL 释放）
 405: py::object dtw_distance_batch(
 406:     ArrD query_arr,
 407:     ArrD candidates_arr,
 408:     int window = 5,
 409:     int top_k = 0
 410: ) {
 411:     auto q = query_arr.unchecked<1>();
 412:     auto c = candidates_arr.unchecked<2>();
 413:     py::ssize_t L = q.shape(0);
 414:     py::ssize_t N = c.shape(0);
 415: 
 416:     if (N == 0) {
 417:         if (top_k > 0) {
 418:             ArrI64 empty_idx(0);
 419:             ArrD empty_dist(0);
 420:             return py::make_tuple(empty_idx, empty_dist);
 421:         }
 422:         ArrD empty_result(0);
 423:         return empty_result;
 424:     }
 425: 
 426:     if (c.shape(1) != L) {
 427:         throw std::invalid_argument(
 428:             "candidates.shape[1] must equal query length, got " +
 429:             std::to_string(c.shape(1)) + " vs " + std::to_string(L));
 430:     }
 431: 
 432:     std::vector<double> distances(N);
 433: 
 434:     {
 435:         py::gil_scoped_release release;
 436:         const double* q_ptr = q.data(0);
 437:         for (py::ssize_t i = 0; i < N; ++i) {
 438:             distances[i] = dtw_distance_span(q_ptr, L, c.data(i, 0), L, window);
 439:         }
 440:     }
 441: 
 442:     if (top_k <= 0 || top_k >= static_cast<int>(N)) {
 443:         ArrD result(N);
 444:         auto res_buf = result.mutable_unchecked<1>();
 445:         for (py::ssize_t i = 0; i < N; ++i) res_buf(i) = distances[i];
 446:         return result;
 447:     }
 448: 
 449:     // Top-K via partial_sort
 450:     std::vector<std::pair<double, py::ssize_t>> indexed;
 451:     indexed.reserve(N);
 452:     for (py::ssize_t i = 0; i < N; ++i) {
 453:         indexed.emplace_back(distances[i], i);
 454:     }
 455:     std::partial_sort(
 456:         indexed.begin(),
 457:         indexed.begin() + top_k,
 458:         indexed.end());
 459: 
 460:     ArrI64 top_indices(top_k);
 461:     ArrD top_dists(top_k);
 462:     auto idx_buf = top_indices.mutable_unchecked<1>();
 463:     auto dist_buf = top_dists.mutable_unchecked<1>();
 464:     for (int i = 0; i < top_k; ++i) {
 465:         idx_buf(i) = static_cast<int64_t>(indexed[i].second);
 466:         dist_buf(i) = indexed[i].first;
 467:     }
 468: 
 469:     return py::make_tuple(top_indices, top_dists);
 470: }
 471: 
 472: // 从 Top-K 有效匹配中提取 15 维特征
 473: PatternResult compute_pattern_features_cpp(
 474:     const std::vector<double>& valid_scores,
 475:     const std::vector<double>& valid_frets,
 476:     const std::vector<py::ssize_t>& valid_ends,
 477:     int T_back
 478: ) {
 479:     PatternResult r{};
 480:     int top_k_actual = static_cast<int>(valid_scores.size());
 481: 
 482:     // F1-F5: 相似度特征
 483:     r.top1_sim = valid_scores[0];
 484:     int n_avg = std::min(5, top_k_actual);
 485:     double sum_avg = 0.0;
 486:     for (int i = 0; i < n_avg; ++i) sum_avg += valid_scores[i];
 487:     r.top5_avg_sim = sum_avg / n_avg;
 488:     r.sim_decay = r.top1_sim - r.top5_avg_sim;
 489: 
 490:     double var = 0.0, mean_s = 0.0;
 491:     for (auto s : valid_scores) mean_s += s;
 492:     mean_s /= top_k_actual;
 493:     for (auto s : valid_scores) var += (s - mean_s) * (s - mean_s);
 494:     r.sim_variance = (top_k_actual > 1) ? var / top_k_actual : 0.0;
 495:     r.match_distance_ratio = (r.top1_sim > 1e-12) ? r.sim_decay / r.top1_sim : 0.0;
 496: 
 497:     // F6-F11: 后续表现
 498:     double sum_fr = 0.0;
 499:     for (auto fr : valid_frets) sum_fr += fr;
 500:     r.avg_future_ret = sum_fr / top_k_actual;
 501: 
 502:     double sum_ws = 0.0, sum_w = 0.0;
 503:     for (int i = 0; i < top_k_actual; ++i) {
 504:         sum_ws += valid_scores[i] * valid_frets[i];
 505:         sum_w += valid_scores[i];
 506:     }
 507:     r.weighted_future_ret = (sum_w > 1e-12) ? sum_ws / sum_w : r.avg_future_ret;
 508: 
 509:     std::vector<double> sorted_fr = valid_frets;
 510:     std::sort(sorted_fr.begin(), sorted_fr.end());
 511:     r.median_future_ret = (top_k_actual % 2 == 1)
 512:         ? sorted_fr[top_k_actual / 2]
 513:         : (sorted_fr[top_k_actual / 2 - 1] + sorted_fr[top_k_actual / 2]) / 2.0;
 514: 
 515:     int pos_count = 0;
 516:     for (auto fr : valid_frets) if (fr > 0) ++pos_count;
 517:     r.ret_sign_consistency = static_cast<double>(pos_count) / top_k_actual;
 518:     r.best_match_ret = valid_frets[0];
 519: 
 520:     double min_fr = *std::min_element(valid_frets.begin(), valid_frets.end());
 521:     r.max_dd_in_matches = std::max(0.0, -min_fr);
 522: 
 523:     // F12-F15: 匹配质量
 524:     auto [min_e, max_e] = std::minmax_element(valid_ends.begin(), valid_ends.end());
 525:     r.match_time_span = static_cast<double>(*max_e - *min_e);
 526:     r.match_time_span_ratio = r.match_time_span / T_back;
 527: 
 528:     std::vector<py::ssize_t> sorted_ends = valid_ends;
 529:     std::sort(sorted_ends.begin(), sorted_ends.end());
 530:     int max_in_window = 0;
 531:     for (int i = 0; i < top_k_actual; ++i) {
 532:         double target = static_cast<double>(sorted_ends[i]) + 60.0;
 533:         auto it = std::upper_bound(sorted_ends.begin(), sorted_ends.end(),
 534:                                    static_cast<py::ssize_t>(target));
 535:         int count = static_cast<int>(it - sorted_ends.begin()) - i;
 536:         max_in_window = std::max(max_in_window, count);
 537:     }
 538:     r.match_cluster_ratio = static_cast<double>(max_in_window) / top_k_actual;
 539: 
 540:     int above = 0;
 541:     for (auto s : valid_scores) if (s > 0.8) ++above;
 542:     r.n_matches_above_thresh = above;
 543: 
 544:     return r;
 545: }
 546: 
 547: // ═══════════════════════════════════════════════════════════════
 548: // 共享核心：余弦预筛选 → DTW 精排 → 特征提取
 549: // single 和 batch 共用此函数，消除 ~400 行重复逻辑
 550: // ═══════════════════════════════════════════════════════════════
 551: std::optional<PatternResult> pattern_match_core(
 552:     const double* prices, py::ssize_t n_prices,
 553:     int T_idx, int k, int L_query, int T_back,
 554:     int match_step, int M_forward, int dtw_window,
 555:     int cos_prefilter_top,
 556:     const std::vector<double>& query_rets,
 557:     py::ssize_t search_start, py::ssize_t search_end,
 558:     const std::vector<std::vector<double>>* precomputed_rets
 559: ) {
 560:     py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());
 561: 
 562:     // ═══ 第1遍：余弦相似度 + 快速形状距离（全量候选）═══
 563:     std::vector<MatchCandidate> cos_candidates;
 564:     std::vector<double> fast_shape_dists;
 565: 
 566:     for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
 567:         py::ssize_t hist_start = hist_end - L_query + 1;
 568:         if (hist_start < 0) continue;
 569: 
 570:         // 获取标准化收益率：缓存优先，否则现场计算
 571:         const std::vector<double>* hist_rets_ptr = nullptr;
 572:         std::vector<double> hist_rets_scratch;
 573: 
 574:         if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size())) {
 575:             hist_rets_ptr = &(*precomputed_rets)[hist_end];
 576:         } else {
 577:             auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
 578:             if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
 579:                 hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query);
 580:                 hist_rets_ptr = &hist_rets_scratch;
 581:             }
 582:         }
 583: 
 584:         if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;
 585: 
 586:         const auto& hist_rets = *hist_rets_ptr;
 587: 
 588:         // 余弦相似度
 589:         double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
 590:         py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
 591:         for (py::ssize_t i = 0; i < min_len; ++i) {
 592:             dot += hist_rets[i] * query_rets[i];
 593:             nx2 += hist_rets[i] * hist_rets[i];
 594:             ny2 += query_rets[i] * query_rets[i];
 595:         }
 596:         double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
 597:         double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;
 598: 
 599:         // 快速形状距离
 600:         double fast_d2 = 0.0;
 601:         for (py::ssize_t i = 0; i < min_len; ++i) {
 602:             double diff = hist_rets[i] - query_rets[i];
 603:             fast_d2 += diff * diff;
 604:         }
 605:         fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));
 606: 
 607:         if (cos_s > 0) {
 608:             cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
 609:         }
 610:     }
 611: 
 612:     if (cos_candidates.size() < 3) return std::nullopt;
 613: 
 614:     // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
 615:     double sigma_fast = 1.0;
 616:     if (fast_shape_dists.size() > 1) {
 617:         double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0.0)
 618:                         / fast_shape_dists.size();
 619:         double var_fd = 0.0;
 620:         for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
 621:         var_fd /= fast_shape_dists.size();
 622:         sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)));
 623:     }
 624:     sigma_fast = std::max(sigma_fast, 1e-12);
 625: 
 626:     // 余弦排序 + 全量边界
 627:     std::sort(cos_candidates.begin(), cos_candidates.end(),
 628:               [](const MatchCandidate& a, const MatchCandidate& b) { return a.cos_s > b.cos_s; });
 629: 
 630:     double global_min_cos = cos_candidates.back().cos_s;
 631:     double global_max_cos = cos_candidates.front().cos_s;
 632: 
 633:     int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
 634:     cos_candidates.resize(n_cos);
 635: 
 636:     // ═══ 第2遍：DTW 精排 (仅 top-N) ═══
 637:     std::vector<double> dtw_dists, cos_sims, future_rets;
 638:     std::vector<py::ssize_t> match_ends;
 639:     dtw_dists.reserve(n_cos);
 640:     cos_sims.reserve(n_cos);
 641:     future_rets.reserve(n_cos);
 642:     match_ends.reserve(n_cos);
 643: 
 644:     for (const auto& cand : cos_candidates) {
 645:         py::ssize_t hn = static_cast<py::ssize_t>(cand.hist_rets.size());
 646:         double dtw_d = dtw_distance_span(cand.hist_rets.data(), hn,
 647:                                           query_rets.data(), n_query, dtw_window);
 648: 
 649:         dtw_dists.push_back(dtw_d);
 650:         cos_sims.push_back(cand.cos_s);
 651: 
 652:         py::ssize_t fut_end = cand.hist_end + M_forward;
 653:         if (fut_end < n_prices && fut_end < T_idx) {
 654:             future_rets.push_back(prices[fut_end] / prices[cand.hist_end] - 1.0);
 655:         } else {
 656:             future_rets.push_back(std::numeric_limits<double>::quiet_NaN());
 657:         }
 658:         match_ends.push_back(cand.hist_end);
 659:     }
 660: 
 661:     if (dtw_dists.size() < 3) return std::nullopt;
 662: 
 663:     // sim_dtw = exp(-dtw/sigma)
 664:     double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;
 665: 
 666:     std::vector<double> sim_dtw(dtw_dists.size());
 667:     double min_dtw_v = std::numeric_limits<double>::max();
 668:     double max_dtw_v = std::numeric_limits<double>::lowest();
 669:     for (size_t i = 0; i < dtw_dists.size(); ++i) {
 670:         sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
 671:         min_dtw_v = std::min(min_dtw_v, sim_dtw[i]);
 672:         max_dtw_v = std::max(max_dtw_v, sim_dtw[i]);
 673:     }
 674: 
 675:     // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
 676:     double range_dtw = (max_dtw_v - min_dtw_v > 1e-12) ? (max_dtw_v - min_dtw_v) : 1.0;
 677:     double range_cos_val = (global_max_cos - global_min_cos > 1e-12)
 678:                            ? (global_max_cos - global_min_cos) : 1.0;
 679: 
 680:     struct Scored { double score, fut_ret; py::ssize_t end_idx; };
 681:     std::vector<Scored> scored;
 682:     scored.reserve(sim_dtw.size());
 683:     for (size_t i = 0; i < sim_dtw.size(); ++i) {
 684:         double nd = (sim_dtw[i] - min_dtw_v) / range_dtw;
 685:         double nc = (cos_sims[i] - global_min_cos) / range_cos_val;
 686:         scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
 687:     }
 688: 
 689:     std::sort(scored.begin(), scored.end(),
 690:               [](const Scored& a, const Scored& b) { return a.score > b.score; });
 691: 
 692:     int top_k = std::min(k, static_cast<int>(scored.size()));
 693: 
 694:     // 过滤 NaN 未来收益
 695:     std::vector<double> valid_scores, valid_frets;
 696:     std::vector<py::ssize_t> valid_ends;
 697:     for (int i = 0; i < top_k; ++i) {
 698:         if (!std::isnan(scored[i].fut_ret)) {
 699:             valid_scores.push_back(scored[i].score);
 700:             valid_frets.push_back(scored[i].fut_ret);
 701:             valid_ends.push_back(scored[i].end_idx);
 702:         }
 703:     }
 704:     if (valid_scores.size() < 2) return std::nullopt;
 705: 
 706:     return compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);
 707: }
 708: 
 709: } // namespace
 710: 
 711: // ═══════════════════════════════════════════════════════════════
 712: // 第六部分-A: 单点形态匹配（薄包装 → pattern_match_core）
 713: // ═══════════════════════════════════════════════════════════════
 714: py::object pattern_match_single(
 715:     ArrD prices_arr,
 716:     int T_idx,
 717:     int k = 10,
 718:     int L_query = 20,
 719:     int T_back = 750,
 720:     int match_step = 1,
 721:     int M_forward = 5,
 722:     int dtw_window = 5,
 723:     int cos_prefilter_top = 50
 724: ) {
 725:     auto prices_buf = prices_arr.unchecked<1>();
 726:     py::ssize_t n_prices = prices_buf.shape(0);
 727:     const double* prices = prices_buf.data(0);
 728: 
 729:     // ── 输入校验 ──
 730:     if (T_idx < 0 || static_cast<py::ssize_t>(T_idx) >= n_prices) {
 731:         throw std::out_of_range("T_idx must satisfy 0 <= T_idx < len(prices), got " + std::to_string(T_idx));
 732:     }
 733:     if (L_query < 3) {
 734:         throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
 735:     }
 736:     if (T_back <= 0) {
 737:         throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
 738:     }
 739:     if (k <= 0) {
 740:         throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
 741:     }
 742:     if (M_forward < 1) {
 743:         throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
 744:     }
 745:     if (match_step <= 0) {
 746:         throw std::invalid_argument("match_step must be > 0");
 747:     }
 748:     if (dtw_window < 0) {
 749:         throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
 750:     }
 751:     if (cos_prefilter_top <= 0) {
 752:         throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
 753:     }
 754:     if (T_idx < L_query + M_forward + 10) return py::none();
 755:     if (T_idx - L_query + 1 < 0) return py::none();
 756: 
 757:     // 查询窗口标准化
 758:     auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
 759:     if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) return py::none();
 760: 
 761:     std::vector<double> query_rets;
 762:     {
 763:         py::gil_scoped_release release;
 764:         query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
 765:     }
 766:     if (query_rets.size() < 2) return py::none();
 767: 
 768:     py::ssize_t search_end = T_idx - L_query;
 769:     if (search_end < L_query) return py::none();
 770:     py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
 771:                                         py::ssize_t(T_idx - T_back));
 772: 
 773:     // ── 委托共享核心（无预计算缓存，现场标准化）──
 774:     std::optional<PatternResult> result_opt;
 775:     {
 776:         py::gil_scoped_release release;
 777:         result_opt = pattern_match_core(
 778:             prices, n_prices, T_idx, k, L_query, T_back,
 779:             match_step, M_forward, dtw_window, cos_prefilter_top,
 780:             query_rets, search_start, search_end,
 781:             nullptr  // 无预计算缓存
 782:         );
 783:     }
 784: 
 785:     if (!result_opt.has_value()) return py::none();
 786: 
 787:     // ── 构造返回值 ──
 788:     py::dict result;
 789:     result["top1_sim"] = result_opt->top1_sim;
 790:     result["top5_avg_sim"] = result_opt->top5_avg_sim;
 791:     result["sim_decay"] = result_opt->sim_decay;
 792:     result["sim_variance"] = result_opt->sim_variance;
 793:     result["match_distance_ratio"] = result_opt->match_distance_ratio;
 794:     result["avg_future_ret"] = result_opt->avg_future_ret;
 795:     result["weighted_future_ret"] = result_opt->weighted_future_ret;
 796:     result["median_future_ret"] = result_opt->median_future_ret;
 797:     result["ret_sign_consistency"] = result_opt->ret_sign_consistency;
 798:     result["best_match_ret"] = result_opt->best_match_ret;
 799:     result["max_dd_in_matches"] = result_opt->max_dd_in_matches;
 800:     result["match_time_span"] = result_opt->match_time_span;
 801:     result["match_time_span_ratio"] = result_opt->match_time_span_ratio;
 802:     result["match_cluster_ratio"] = result_opt->match_cluster_ratio;
 803:     result["n_matches_above_thresh"] = result_opt->n_matches_above_thresh;
 804:     return result;
 805: }
 806: 
 807: // ═══════════════════════════════════════════════════════════════
 808: // 第七部分: 批量形态匹配 (v3 新增)
 809: // ═══════════════════════════════════════════════════════════════
 810: 

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 '"'src/cpp/etf_core.cpp'; for ("'$i=472; $i -le 713; $i++) { '"'{0,4}: {1}' -f "'$i, $lines[$i-1] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 184ms:
 472: // 从 Top-K 有效匹配中提取 15 维特征
 473: PatternResult compute_pattern_features_cpp(
 474:     const std::vector<double>& valid_scores,
 475:     const std::vector<double>& valid_frets,
 476:     const std::vector<py::ssize_t>& valid_ends,
 477:     int T_back
 478: ) {
 479:     PatternResult r{};
 480:     int top_k_actual = static_cast<int>(valid_scores.size());
 481: 
 482:     // F1-F5: 相似度特征
 483:     r.top1_sim = valid_scores[0];
 484:     int n_avg = std::min(5, top_k_actual);
 485:     double sum_avg = 0.0;
 486:     for (int i = 0; i < n_avg; ++i) sum_avg += valid_scores[i];
 487:     r.top5_avg_sim = sum_avg / n_avg;
 488:     r.sim_decay = r.top1_sim - r.top5_avg_sim;
 489: 
 490:     double var = 0.0, mean_s = 0.0;
 491:     for (auto s : valid_scores) mean_s += s;
 492:     mean_s /= top_k_actual;
 493:     for (auto s : valid_scores) var += (s - mean_s) * (s - mean_s);
 494:     r.sim_variance = (top_k_actual > 1) ? var / top_k_actual : 0.0;
 495:     r.match_distance_ratio = (r.top1_sim > 1e-12) ? r.sim_decay / r.top1_sim : 0.0;
 496: 
 497:     // F6-F11: 后续表现
 498:     double sum_fr = 0.0;
 499:     for (auto fr : valid_frets) sum_fr += fr;
 500:     r.avg_future_ret = sum_fr / top_k_actual;
 501: 
 502:     double sum_ws = 0.0, sum_w = 0.0;
 503:     for (int i = 0; i < top_k_actual; ++i) {
 504:         sum_ws += valid_scores[i] * valid_frets[i];
 505:         sum_w += valid_scores[i];
 506:     }
 507:     r.weighted_future_ret = (sum_w > 1e-12) ? sum_ws / sum_w : r.avg_future_ret;
 508: 
 509:     std::vector<double> sorted_fr = valid_frets;
 510:     std::sort(sorted_fr.begin(), sorted_fr.end());
 511:     r.median_future_ret = (top_k_actual % 2 == 1)
 512:         ? sorted_fr[top_k_actual / 2]
 513:         : (sorted_fr[top_k_actual / 2 - 1] + sorted_fr[top_k_actual / 2]) / 2.0;
 514: 
 515:     int pos_count = 0;
 516:     for (auto fr : valid_frets) if (fr > 0) ++pos_count;
 517:     r.ret_sign_consistency = static_cast<double>(pos_count) / top_k_actual;
 518:     r.best_match_ret = valid_frets[0];
 519: 
 520:     double min_fr = *std::min_element(valid_frets.begin(), valid_frets.end());
 521:     r.max_dd_in_matches = std::max(0.0, -min_fr);
 522: 
 523:     // F12-F15: 匹配质量
 524:     auto [min_e, max_e] = std::minmax_element(valid_ends.begin(), valid_ends.end());
 525:     r.match_time_span = static_cast<double>(*max_e - *min_e);
 526:     r.match_time_span_ratio = r.match_time_span / T_back;
 527: 
 528:     std::vector<py::ssize_t> sorted_ends = valid_ends;
 529:     std::sort(sorted_ends.begin(), sorted_ends.end());
 530:     int max_in_window = 0;
 531:     for (int i = 0; i < top_k_actual; ++i) {
 532:         double target = static_cast<double>(sorted_ends[i]) + 60.0;
 533:         auto it = std::upper_bound(sorted_ends.begin(), sorted_ends.end(),
 534:                                    static_cast<py::ssize_t>(target));
 535:         int count = static_cast<int>(it - sorted_ends.begin()) - i;
 536:         max_in_window = std::max(max_in_window, count);
 537:     }
 538:     r.match_cluster_ratio = static_cast<double>(max_in_window) / top_k_actual;
 539: 
 540:     int above = 0;
 541:     for (auto s : valid_scores) if (s > 0.8) ++above;
 542:     r.n_matches_above_thresh = above;
 543: 
 544:     return r;
 545: }
 546: 
 547: // ═══════════════════════════════════════════════════════════════
 548: // 共享核心：余弦预筛选 → DTW 精排 → 特征提取
 549: // single 和 batch 共用此函数，消除 ~400 行重复逻辑
 550: // ═══════════════════════════════════════════════════════════════
 551: std::optional<PatternResult> pattern_match_core(
 552:     const double* prices, py::ssize_t n_prices,
 553:     int T_idx, int k, int L_query, int T_back,
 554:     int match_step, int M_forward, int dtw_window,
 555:     int cos_prefilter_top,
 556:     const std::vector<double>& query_rets,
 557:     py::ssize_t search_start, py::ssize_t search_end,
 558:     const std::vector<std::vector<double>>* precomputed_rets
 559: ) {
 560:     py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());
 561: 
 562:     // ═══ 第1遍：余弦相似度 + 快速形状距离（全量候选）═══
 563:     std::vector<MatchCandidate> cos_candidates;
 564:     std::vector<double> fast_shape_dists;
 565: 
 566:     for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
 567:         py::ssize_t hist_start = hist_end - L_query + 1;
 568:         if (hist_start < 0) continue;
 569: 
 570:         // 获取标准化收益率：缓存优先，否则现场计算
 571:         const std::vector<double>* hist_rets_ptr = nullptr;
 572:         std::vector<double> hist_rets_scratch;
 573: 
 574:         if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size())) {
 575:             hist_rets_ptr = &(*precomputed_rets)[hist_end];
 576:         } else {
 577:             auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
 578:             if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
 579:                 hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query);
 580:                 hist_rets_ptr = &hist_rets_scratch;
 581:             }
 582:         }
 583: 
 584:         if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;
 585: 
 586:         const auto& hist_rets = *hist_rets_ptr;
 587: 
 588:         // 余弦相似度
 589:         double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
 590:         py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
 591:         for (py::ssize_t i = 0; i < min_len; ++i) {
 592:             dot += hist_rets[i] * query_rets[i];
 593:             nx2 += hist_rets[i] * hist_rets[i];
 594:             ny2 += query_rets[i] * query_rets[i];
 595:         }
 596:         double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
 597:         double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;
 598: 
 599:         // 快速形状距离
 600:         double fast_d2 = 0.0;
 601:         for (py::ssize_t i = 0; i < min_len; ++i) {
 602:             double diff = hist_rets[i] - query_rets[i];
 603:             fast_d2 += diff * diff;
 604:         }
 605:         fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));
 606: 
 607:         if (cos_s > 0) {
 608:             cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
 609:         }
 610:     }
 611: 
 612:     if (cos_candidates.size() < 3) return std::nullopt;
 613: 
 614:     // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
 615:     double sigma_fast = 1.0;
 616:     if (fast_shape_dists.size() > 1) {
 617:         double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0.0)
 618:                         / fast_shape_dists.size();
 619:         double var_fd = 0.0;
 620:         for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
 621:         var_fd /= fast_shape_dists.size();
 622:         sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)));
 623:     }
 624:     sigma_fast = std::max(sigma_fast, 1e-12);
 625: 
 626:     // 余弦排序 + 全量边界
 627:     std::sort(cos_candidates.begin(), cos_candidates.end(),
 628:               [](const MatchCandidate& a, const MatchCandidate& b) { return a.cos_s > b.cos_s; });
 629: 
 630:     double global_min_cos = cos_candidates.back().cos_s;
 631:     double global_max_cos = cos_candidates.front().cos_s;
 632: 
 633:     int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
 634:     cos_candidates.resize(n_cos);
 635: 
 636:     // ═══ 第2遍：DTW 精排 (仅 top-N) ═══
 637:     std::vector<double> dtw_dists, cos_sims, future_rets;
 638:     std::vector<py::ssize_t> match_ends;
 639:     dtw_dists.reserve(n_cos);
 640:     cos_sims.reserve(n_cos);
 641:     future_rets.reserve(n_cos);
 642:     match_ends.reserve(n_cos);
 643: 
 644:     for (const auto& cand : cos_candidates) {
 645:         py::ssize_t hn = static_cast<py::ssize_t>(cand.hist_rets.size());
 646:         double dtw_d = dtw_distance_span(cand.hist_rets.data(), hn,
 647:                                           query_rets.data(), n_query, dtw_window);
 648: 
 649:         dtw_dists.push_back(dtw_d);
 650:         cos_sims.push_back(cand.cos_s);
 651: 
 652:         py::ssize_t fut_end = cand.hist_end + M_forward;
 653:         if (fut_end < n_prices && fut_end < T_idx) {
 654:             future_rets.push_back(prices[fut_end] / prices[cand.hist_end] - 1.0);
 655:         } else {
 656:             future_rets.push_back(std::numeric_limits<double>::quiet_NaN());
 657:         }
 658:         match_ends.push_back(cand.hist_end);
 659:     }
 660: 
 661:     if (dtw_dists.size() < 3) return std::nullopt;
 662: 
 663:     // sim_dtw = exp(-dtw/sigma)
 664:     double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;
 665: 
 666:     std::vector<double> sim_dtw(dtw_dists.size());
 667:     double min_dtw_v = std::numeric_limits<double>::max();
 668:     double max_dtw_v = std::numeric_limits<double>::lowest();
 669:     for (size_t i = 0; i < dtw_dists.size(); ++i) {
 670:         sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
 671:         min_dtw_v = std::min(min_dtw_v, sim_dtw[i]);
 672:         max_dtw_v = std::max(max_dtw_v, sim_dtw[i]);
 673:     }
 674: 
 675:     // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
 676:     double range_dtw = (max_dtw_v - min_dtw_v > 1e-12) ? (max_dtw_v - min_dtw_v) : 1.0;
 677:     double range_cos_val = (global_max_cos - global_min_cos > 1e-12)
 678:                            ? (global_max_cos - global_min_cos) : 1.0;
 679: 
 680:     struct Scored { double score, fut_ret; py::ssize_t end_idx; };
 681:     std::vector<Scored> scored;
 682:     scored.reserve(sim_dtw.size());
 683:     for (size_t i = 0; i < sim_dtw.size(); ++i) {
 684:         double nd = (sim_dtw[i] - min_dtw_v) / range_dtw;
 685:         double nc = (cos_sims[i] - global_min_cos) / range_cos_val;
 686:         scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
 687:     }
 688: 
 689:     std::sort(scored.begin(), scored.end(),
 690:               [](const Scored& a, const Scored& b) { return a.score > b.score; });
 691: 
 692:     int top_k = std::min(k, static_cast<int>(scored.size()));
 693: 
 694:     // 过滤 NaN 未来收益
 695:     std::vector<double> valid_scores, valid_frets;
 696:     std::vector<py::ssize_t> valid_ends;
 697:     for (int i = 0; i < top_k; ++i) {
 698:         if (!std::isnan(scored[i].fut_ret)) {
 699:             valid_scores.push_back(scored[i].score);
 700:             valid_frets.push_back(scored[i].fut_ret);
 701:             valid_ends.push_back(scored[i].end_idx);
 702:         }
 703:     }
 704:     if (valid_scores.size() < 2) return std::nullopt;
 705: 
 706:     return compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);
 707: }
 708: 
 709: } // namespace
 710: 
 711: // ═══════════════════════════════════════════════════════════════
 712: // 第六部分-A: 单点形态匹配（薄包装 → pattern_match_core）
 713: // ═══════════════════════════════════════════════════════════════

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 '"'src/cpp/etf_core.cpp'; for ("'$i=560; $i -le 625; $i++) { '"'{0,4}: {1}' -f "'$i, $lines[$i-1] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 172ms:
 560:     py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());
 561: 
 562:     // ═══ 第1遍：余弦相似度 + 快速形状距离（全量候选）═══
 563:     std::vector<MatchCandidate> cos_candidates;
 564:     std::vector<double> fast_shape_dists;
 565: 
 566:     for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
 567:         py::ssize_t hist_start = hist_end - L_query + 1;
 568:         if (hist_start < 0) continue;
 569: 
 570:         // 获取标准化收益率：缓存优先，否则现场计算
 571:         const std::vector<double>* hist_rets_ptr = nullptr;
 572:         std::vector<double> hist_rets_scratch;
 573: 
 574:         if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size())) {
 575:             hist_rets_ptr = &(*precomputed_rets)[hist_end];
 576:         } else {
 577:             auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
 578:             if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
 579:                 hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query);
 580:                 hist_rets_ptr = &hist_rets_scratch;
 581:             }
 582:         }
 583: 
 584:         if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;
 585: 
 586:         const auto& hist_rets = *hist_rets_ptr;
 587: 
 588:         // 余弦相似度
 589:         double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
 590:         py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
 591:         for (py::ssize_t i = 0; i < min_len; ++i) {
 592:             dot += hist_rets[i] * query_rets[i];
 593:             nx2 += hist_rets[i] * hist_rets[i];
 594:             ny2 += query_rets[i] * query_rets[i];
 595:         }
 596:         double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
 597:         double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;
 598: 
 599:         // 快速形状距离
 600:         double fast_d2 = 0.0;
 601:         for (py::ssize_t i = 0; i < min_len; ++i) {
 602:             double diff = hist_rets[i] - query_rets[i];
 603:             fast_d2 += diff * diff;
 604:         }
 605:         fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));
 606: 
 607:         if (cos_s > 0) {
 608:             cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
 609:         }
 610:     }
 611: 
 612:     if (cos_candidates.size() < 3) return std::nullopt;
 613: 
 614:     // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
 615:     double sigma_fast = 1.0;
 616:     if (fast_shape_dists.size() > 1) {
 617:         double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0.0)
 618:                         / fast_shape_dists.size();
 619:         double var_fd = 0.0;
 620:         for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
 621:         var_fd /= fast_shape_dists.size();
 622:         sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)));
 623:     }
 624:     sigma_fast = std::max(sigma_fast, 1e-12);
 625: 

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 '"'src/cpp/etf_core.cpp'; for ("'$i=811; $i -le 1005; $i++) { '"'{0,4}: {1}' -f "'$i, $lines[$i-1] }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 180ms:
 811: py::tuple pattern_match_batch(
 812:     ArrD prices_arr,
 813:     ArrI64 t_indices_arr,
 814:     int k = 10,
 815:     int L_query = 20,
 816:     int T_back = 750,
 817:     int match_step = 1,
 818:     int M_forward = 5,
 819:     int dtw_window = 5,
 820:     int cos_prefilter_top = 50
 821: ) {
 822:     auto prices_buf = prices_arr.unchecked<1>();
 823:     py::ssize_t n_prices = prices_buf.shape(0);
 824:     const double* prices = prices_buf.data(0);
 825: 
 826:     auto t_buf = t_indices_arr.unchecked<1>();
 827:     py::ssize_t n_samples = t_buf.shape(0);
 828:     const int64_t* t_ptr = t_buf.data(0);
 829: 
 830:     // ── 输入校验 ──
 831:     if (L_query < 3) {
 832:         throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
 833:     }
 834:     if (T_back <= 0) {
 835:         throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
 836:     }
 837:     if (k <= 0) {
 838:         throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
 839:     }
 840:     if (M_forward < 1) {
 841:         throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
 842:     }
 843:     if (match_step <= 0) {
 844:         throw std::invalid_argument("match_step must be > 0");
 845:     }
 846:     if (dtw_window < 0) {
 847:         throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
 848:     }
 849:     if (cos_prefilter_top <= 0) {
 850:         throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
 851:     }
 852:     if (n_samples == 0) {
 853:         ArrD empty_features(std::vector<py::ssize_t>{0, 15});
 854:         py::array_t<bool> empty_mask(std::vector<py::ssize_t>{0});
 855:         return py::make_tuple(empty_features, empty_mask);
 856:     }
 857: 
 858:     for (py::ssize_t i = 1; i < n_samples; ++i) {
 859:         if (t_ptr[i] <= t_ptr[i - 1]) {
 860:             throw std::invalid_argument("t_indices must be strictly increasing");
 861:         }
 862:     }
 863:     if (t_ptr[n_samples - 1] >= n_prices) {
 864:         throw std::invalid_argument("max(t_indices) must be < len(prices)");
 865:     }
 866: 
 867:     std::vector<double> features_flat;
 868:     features_flat.reserve(n_samples * 15);
 869:     std::vector<bool> valid_mask(n_samples, false);
 870: 
 871:     {
 872:         // ── GIL 释放区：纯 C++ 批量计算 ──
 873:         py::gil_scoped_release release;
 874: 
 875:         // ── 第一遍：计算所有 T_idx 搜索范围的并集（避免预计算无用窗口）──
 876:         py::ssize_t precompute_start = n_prices;
 877:         py::ssize_t precompute_end = 0;
 878:         for (py::ssize_t s = 0; s < n_samples; ++s) {
 879:             int T_idx = static_cast<int>(t_ptr[s]);
 880:             if (T_idx < L_query + M_forward + 10) continue;
 881:             py::ssize_t s_end = T_idx - L_query;
 882:             if (s_end < L_query) continue;
 883:             py::ssize_t s_start = std::max(py::ssize_t(L_query - 1),
 884:                                            py::ssize_t(T_idx - T_back));
 885:             if (s_start < s_end) {
 886:                 precompute_start = std::min(precompute_start, s_start);
 887:                 precompute_end = std::max(precompute_end, s_end);
 888:             }
 889:         }
 890: 
 891:         // ── 仅预计算搜索范围并集内的窗口标准化收益率 ──
 892:         std::vector<std::vector<double>> precomputed_rets(n_prices);
 893:         if (precompute_start <= precompute_end) {
 894:             for (py::ssize_t end = precompute_start; end <= precompute_end; ++end) {
 895:                 py::ssize_t start = end - L_query + 1;
 896:                 if (start >= 0) {
 897:                     auto window_prices = extract_window(prices, start, end);
 898:                     precomputed_rets[end] = standardize_returns_cpp(window_prices.data(), L_query);
 899:                 }
 900:             }
 901:         }
 902: 
 903:         // ── 对每个 T_idx 执行形态匹配（复用预计算缓存）──
 904:         for (py::ssize_t s = 0; s < n_samples; ++s) {
 905:             int T_idx = static_cast<int>(t_ptr[s]);
 906: 
 907:             if (T_idx < L_query + M_forward + 10) continue;
 908:             if (T_idx - L_query + 1 < 0) continue;
 909: 
 910:             auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
 911:             if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) continue;
 912: 
 913:             auto query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
 914:             if (query_rets.size() < 2) continue;
 915: 
 916:             py::ssize_t search_end = T_idx - L_query;
 917:             if (search_end < L_query) continue;
 918:             py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
 919:                                                 py::ssize_t(T_idx - T_back));
 920: 
 921:             // ── 委托共享核心（使用预计算缓存）──
 922:             auto result_opt = pattern_match_core(
 923:                 prices, n_prices, T_idx, k, L_query, T_back,
 924:                 match_step, M_forward, dtw_window, cos_prefilter_top,
 925:                 query_rets, search_start, search_end,
 926:                 &precomputed_rets
 927:             );
 928: 
 929:             if (!result_opt.has_value()) continue;
 930: 
 931:             auto& r = *result_opt;
 932:             features_flat.push_back(r.top1_sim);
 933:             features_flat.push_back(r.top5_avg_sim);
 934:             features_flat.push_back(r.sim_decay);
 935:             features_flat.push_back(r.sim_variance);
 936:             features_flat.push_back(r.match_distance_ratio);
 937:             features_flat.push_back(r.avg_future_ret);
 938:             features_flat.push_back(r.weighted_future_ret);
 939:             features_flat.push_back(r.median_future_ret);
 940:             features_flat.push_back(r.ret_sign_consistency);
 941:             features_flat.push_back(r.best_match_ret);
 942:             features_flat.push_back(r.max_dd_in_matches);
 943:             features_flat.push_back(r.match_time_span);
 944:             features_flat.push_back(r.match_time_span_ratio);
 945:             features_flat.push_back(r.match_cluster_ratio);
 946:             features_flat.push_back(static_cast<double>(r.n_matches_above_thresh));
 947: 
 948:             valid_mask[s] = true;
 949:         }
 950:     } // GIL 在此重新获取
 951: 
 952:     // ── 构造返回数组 ──
 953:     py::ssize_t n_valid = static_cast<py::ssize_t>(features_flat.size()) / 15;
 954:     ArrD features_X15(std::vector<py::ssize_t>{n_valid, 15});
 955:     auto fx_buf = features_X15.mutable_unchecked<2>();
 956:     for (py::ssize_t i = 0; i < n_valid; ++i) {
 957:         for (py::ssize_t j = 0; j < 15; ++j) {
 958:             fx_buf(i, j) = features_flat[i * 15 + j];
 959:         }
 960:     }
 961: 
 962:     py::array_t<bool> valid_mask_arr(std::vector<py::ssize_t>{n_samples});
 963:     auto vm_buf = valid_mask_arr.mutable_unchecked<1>();
 964:     for (py::ssize_t i = 0; i < n_samples; ++i) {
 965:         vm_buf(i) = valid_mask[i];
 966:     }
 967: 
 968:     return py::make_tuple(features_X15, valid_mask_arr);
 969: }
 970: 
 971: // ═══════════════════════════════════════════════════════════════
 972: // 模块定义
 973: // ═══════════════════════════════════════════════════════════════
 974: 
 975: PYBIND11_MODULE(etf_core, m) {
 976:     m.doc() = "ETF pattern matching core — C++ accelerated (pybind11)\n\n"
 977:               "来源: 形态匹配ETF组合策略_V3.3.py\n"
 978:               "模块: dtw_distance, standardize_returns, cosine_similarity,\n"
 979:               "       compute_adx, compute_atr, dtw_distance_batch,\n"
 980:               "       pattern_match_single, pattern_match_batch\n"
 981:               "v2: 三模块合并为单一 etf_core, /utf-8, py::ssize_t, forcecast\n"
 982:               "v3: 新增 pattern_match_batch，支持同 ETF 多 T_idx 批量形态匹配";
 983: 
 984:     // ── 序列预处理 ──
 985:     m.def("standardize_returns", &standardize_returns,
 986:           py::arg("price_series"),
 987:           "计算标准化收益率序列: (rets - mean) / std.\n\n"
 988:           "Args: price_series (1-D float64 array, n>=2)\n"
 989:           "Returns: 1-D float64 array (length n-1)");
 990: 
 991:     m.def("cosine_similarity", &cosine_similarity,
 992:           py::arg("x"), py::arg("y"),
 993:           "两向量余弦相似度 ∈ [-1, 1].\n"
 994:           "norm < 1e-12 时返回 0.0.");
 995: 
 996:     // ── DTW ──
 997:     m.def("dtw_distance", &dtw_distance,
 998:           py::arg("x"), py::arg("y"), py::arg("window") = 5,
 999:           "Sakoe-Chiba band DTW 距离.\n"
1000:           "返回归一化距离: sqrt(dtw[n,m]) / (n+m).\n"
1001:           "空序列返回 inf.");
1002: 
1003:     m.def("dtw_distance_batch", &dtw_distance_batch,
1004:           py::arg("query"), py::arg("candidates"),
1005:           py::arg("window") = 5, py::arg("top_k") = 0,

mcp: node_repl/js started
mcp: node_repl/js (failed)
tool call error: tool call failed for `node_repl/js`

Caused by:
    Mcp error: -32602: js: codex/sandbox-state-meta: missing field `sandboxPolicy`
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "python -c 'from pathlib import Path; content = r\"\"\"/**
 * test_etf_core.cpp — etf_core 原生 C++ 算法测试
 *
 * 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17
 */

#define DOCTEST_CONFIG_IMPLEMENT
#include <doctest/doctest.h>

#include <pybind11/embed.h>
#include <pybind11/numpy.h>

#include <array>
#include <cmath>
#include <cstdint>
#include <limits>
#include <stdexcept>
#include <vector>

namespace py = pybind11;

using ArrD = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;

// etf_core.cpp 当前没有公共 C++ 头文件，因此在此声明原生入口。
// 测试直接调用这些符号，不导入 Python 扩展模块，也不测试绑定分发层。
ArrD standardize_returns(ArrD price_series);
double cosine_similarity(ArrD x_arr, ArrD y_arr);
double dtw_distance(ArrD x_arr, ArrD y_arr, int window);
py::object dtw_distance_batch(ArrD query_arr, ArrD candidates_arr, int window, int top_k);
double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
py::object pattern_match_single(
    ArrD prices_arr,
    int T_idx,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);
py::tuple pattern_match_batch(
    ArrD prices_arr,
    ArrI64 t_indices_arr,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);

// 非有限值策略（由 etf_core.cpp 的当前实现定义）：
// 1. standardize_returns 对价格窗口执行有限性检查；任一 NaN/Inf 都拒绝整个窗口并返回空数组。
// 2. cosine_similarity 与 DTW 不预先拒绝 NaN/Inf，而是按 IEEE-754 传播；Inf/Inf 等不定式产生 NaN。
// 3. compute_adx 与 compute_atr 不预先拒绝 NaN/Inf；ADX 中 Inf/Inf 可变为 NaN，ATR 保留 NaN/Inf。
// 4. pattern_match_single/batch 通过标准化步骤拒绝含 NaN/Inf 的查询窗口；single 返回 None，batch 标记无效。

namespace {

constexpr int kPatternTIdx = 30;
constexpr int kPatternK = 50;
constexpr int kPatternQueryLength = 3;
constexpr int kPatternLookback = 100;
constexpr int kPatternStep = 1;
constexpr int kPatternForward = 1;
constexpr int kPatternDtwWindow = 1;
constexpr int kPatternPrefilterTop = 50;

constexpr std::array<const char*, 15> kFeatureKeys = {
    \"top1_sim\",
    \"top5_avg_sim\",
    \"sim_decay\",
    \"sim_variance\",
    \"match_distance_ratio\",
    \"avg_future_ret\",
    \"weighted_future_ret\",
    \"median_future_ret\",
    \"ret_sign_consistency\",
    \"best_match_ret\",
    \"max_dd_in_matches\",
    \"match_time_span\",
    \"match_time_span_ratio\",
    \"match_cluster_ratio\",
    \"n_matches_above_thresh\",
};

constexpr std::array<double, 15> kPeriodicExpectedFeatures = {
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    0.0,
    24.0,
    0.24,
    1.0,
    0.0,
};

ArrD make_array(const std::vector<double>& values) {
    ArrD result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_array(std::initializer_list<double> values) {
    return make_array(std::vector<double>(values));
}

ArrI64 make_index_array(const std::vector<int64_t>& values) {
    ArrI64 result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    const std::vector<double>& values) {
    if (values.size() "'!= static_cast<std::size_t>(rows * cols)) {
        throw std::invalid_argument("matrix data size does not match shape");
    }

    ArrD result(std::vector<py::ssize_t>{rows, cols});
    auto out = result.mutable_unchecked<2>();
    for (py::ssize_t row = 0; row < rows; ++row) {
        for (py::ssize_t col = 0; col < cols; ++col) {
            out(row, col) = values[static_cast<std::size_t>(row * cols + col)];
        }
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    std::initializer_list<double> values) {
    return make_matrix(rows, cols, std::vector<double>(values));
}

std::vector<double> make_periodic_prices(double scale) {
    std::vector<double> prices(41);
    prices[0] = scale;
    for (std::size_t i = 1; i < prices.size(); ++i) {
        const double factor = ((i - 1) % 2 == 0) ? 2.0 : 4.0;
        prices[i] = prices[i - 1] * factor;
    }
    return prices;
}

struct OhlcVectors {
    std::vector<double> high;
    std::vector<double> low;
    std::vector<double> close;
};

OhlcVectors make_trending_ohlc(double scale) {
    OhlcVectors data;
    data.high.resize(18);
    data.low.resize(18);
    data.close.resize(18);

    for (std::size_t i = 0; i < data.close.size(); ++i) {
        data.close[i] = (static_cast<double>(i) + 2.0) * scale;
        data.high[i] = data.close[i] + 0.5 * scale;
        data.low[i] = data.close[i] - 0.5 * scale;
    }
    return data;
}

OhlcVectors make_known_atr_input(double scale = 1.0) {
    return {
        {10.0 * scale, 12.0 * scale, 13.0 * scale, 15.0 * scale},
        {8.0 * scale, 9.0 * scale, 11.0 * scale, 12.0 * scale},
        {9.0 * scale, 11.0 * scale, 12.0 * scale, 14.0 * scale},
    };
}

py::object run_pattern_single(const std::vector<double>& prices, int t_idx = kPatternTIdx) {
    return pattern_match_single(
        make_array(prices),
        t_idx,
        kPatternK,
        kPatternQueryLength,
        kPatternLookback,
        kPatternStep,
        kPatternForward,
        kPatternDtwWindow,
        kPatternPrefilterTop);
}

py::tuple run_pattern_batch(
    const std::vector<double>& prices,
    const std::vector<int64_t>& t_indices) {
    return pattern_match_batch(
        make_array(prices),
        make_index_array(t_indices),
        kPatternK,
        kPatternQueryLength,
        kPatternLookback,
        kPatternStep,
        kPatternForward,
        kPatternDtwWindow,
        kPatternPrefilterTop);
}

std::array<double, 15> values_from_dict(const py::dict& result) {
    std::array<double, 15> values{};
    for (std::size_t i = 0; i < kFeatureKeys.size(); ++i) {
        values[i] = py::cast<double>(result[py::str(kFeatureKeys[i])]);
    }
    return values;
}

std::array<double, 15> values_from_batch_row(const ArrD& features, py::ssize_t row) {
    const auto data = features.unchecked<2>();
    std::array<double, 15> values{};
    for (py::ssize_t col = 0; col < 15; ++col) {
        values[static_cast<std::size_t>(col)] = data(row, col);
    }
    return values;
}

void check_periodic_expected_features(const std::array<double, 15>& actual) {
    for (std::size_t i = 0; i < actual.size(); ++i) {
        CAPTURE(i);
        CHECK(actual[i] == doctest::Approx(kPeriodicExpectedFeatures[i]).epsilon(1e-12));
    }
}

} // namespace

int main(int argc, char** argv) {
    py::scoped_interpreter interpreter{};
    doctest::Context context(argc, argv);
    return context.run();
}

TEST_CASE("standardize_returns covers edge cases and a hand-computed result") {
    SUBCASE("empty input returns an empty array") {
        const ArrD result = standardize_returns(make_array({}));
        CHECK(result.ndim() == 1);
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("single price returns an empty array") {
        const ArrD result = standardize_returns(make_array({42.0}));
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("NaN and Inf reject the whole price window") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(standardize_returns(make_array({1.0, nan, 2.0})).shape(0) == 0);
        CHECK(standardize_returns(make_array({1.0, inf, 2.0})).shape(0) == 0);
    }

    SUBCASE("very small prices are floored and become zero returns") {
        const double tiny = std::ldexp(1.0, -900);
        const ArrD result = standardize_returns(make_array({tiny, 2.0 * tiny, 8.0 * tiny}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(0.0));
        CHECK(out(1) == doctest::Approx(0.0));
    }

    SUBCASE("very large finite prices remain numerically stable") {
        const double huge = std::ldexp(1.0, 900);
        const ArrD result = standardize_returns(make_array({huge, 2.0 * huge, 8.0 * huge}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(-1.0).epsilon(1e-12));
        CHECK(out(1) == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known answer for prices 1, 2, 8 is -1, 1") {
        const ArrD result = standardize_returns(make_array({1.0, 2.0, 8.0}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(-1.0).epsilon(1e-12));
        CHECK(out(1) == doctest::Approx(1.0).epsilon(1e-12));
    }
}

TEST_CASE("cosine_similarity covers edge cases and a hand-computed result") {
    SUBCASE("empty vectors return the neutral similarity zero") {
        CHECK(cosine_similarity(make_array({}), make_array({})) == doctest::Approx(0.0));
    }

    SUBCASE("single positive elements have similarity one") {
        CHECK(cosine_similarity(make_array({2.0}), make_array({3.0})) == doctest::Approx(1.0));
    }

    SUBCASE("NaN and Inf propagate to NaN") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(std::isnan(cosine_similarity(make_array({nan}), make_array({1.0}))));
        CHECK(std::isnan(cosine_similarity(make_array({inf}), make_array({1.0}))));
    }

    SUBCASE("very small norm returns zero and huge squaring overflow returns NaN") {
        CHECK(cosine_similarity(make_array({1e-300}), make_array({1.0})) == doctest::Approx(0.0));
        CHECK(std::isnan(cosine_similarity(make_array({1e308}), make_array({1e308}))));
    }

    SUBCASE("known answer is four fifths") {
        CHECK(cosine_similarity(make_array({1.0, 2.0}), make_array({2.0, 1.0}))
              == doctest::Approx(0.8).epsilon(1e-12));
    }

    SUBCASE("mismatched lengths are rejected") {
        CHECK_THROWS_AS(
            cosine_similarity(make_array({1.0}), make_array({1.0, 2.0})),
            std::invalid_argument);
    }
}

TEST_CASE("dtw_distance covers ties, window boundaries, and numeric policies") {
    SUBCASE("an empty sequence returns infinity") {
        CHECK(std::isinf(dtw_distance(make_array({}), make_array({1.0}), 1)));
        CHECK(std::isinf(dtw_distance(make_array({1.0}), make_array({}), 1)));
    }

    SUBCASE("single elements use sqrt squared cost divided by total length") {
        CHECK(dtw_distance(make_array({2.0}), make_array({5.0}), 0)
              == doctest::Approx(1.5).epsilon(1e-12));
    }

    SUBCASE("NaN propagates and finite versus Inf returns Inf") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(std::isnan(dtw_distance(make_array({nan}), make_array({0.0}), 0)));
        CHECK(std::isinf(dtw_distance(make_array({inf}), make_array({0.0}), 0)));
    }

    SUBCASE("very large and very small finite costs remain representable") {
        CHECK(dtw_distance(make_array({1e150}), make_array({-1e150}), 0)
              == doctest::Approx(1e150).epsilon(1e-12));
        CHECK(dtw_distance(make_array({1e-150}), make_array({-1e-150}), 0) / 1e-150
              == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known diagonal answer is one quarter") {
        CHECK(dtw_distance(make_array({0.0, 1.0}), make_array({0.0, 2.0}), 0)
              == doctest::Approx(0.25).epsilon(1e-12));
    }

    SUBCASE("equal predecessor ties stay deterministic in distance") {
        CHECK(dtw_distance(make_array({0.0, 0.0}), make_array({0.0, 0.0, 0.0}), 0)
              == doctest::Approx(0.0));
    }

    SUBCASE("window zero enforces the diagonal and window one permits warping") {
        const ArrD x = make_array({0.0, 1.0, 1.0});
        const ArrD y = make_array({0.0, 0.0, 1.0});
        CHECK(dtw_distance(x, y, 0) == doctest::Approx(1.0 / 6.0).epsilon(1e-12));
        CHECK(dtw_distance(x, y, 1) == doctest::Approx(0.0));
    }
}

TEST_CASE("dtw_distance_batch matches scalar DTW and honors Top-K ties") {
    SUBCASE("empty candidates return empty arrays in both modes") {
        const py::object all_result = dtw_distance_batch(
            make_array({}), make_matrix(0, 0, {}), 0, 0);
        const ArrD all_distances = py::reinterpret_borrow<ArrD>(all_result);
        CHECK(all_distances.shape(0) == 0);

        const py::object top_result = dtw_distance_batch(
            make_array({}), make_matrix(0, 0, {}), 0, 1);
        REQUIRE(py::isinstance<py::tuple>(top_result));
        const py::tuple top = py::reinterpret_borrow<py::tuple>(top_result);
        const ArrI64 indices = top[0].cast<ArrI64>();
        const ArrD distances = top[1].cast<ArrD>();
        CHECK(indices.shape(0) == 0);
        CHECK(distances.shape(0) == 0);
    }

    SUBCASE("one query value and one candidate produce the scalar answer") {
        const py::object result = dtw_distance_batch(
            make_array({2.0}), make_matrix(1, 1, {5.0}), 0, 0);
        const ArrD distances = py::reinterpret_borrow<ArrD>(result);
        const auto out = distances.unchecked<1>();
        REQUIRE(out.shape(0) == 1);
        CHECK(out(0) == doctest::Approx(1.5).epsilon(1e-12));
    }

    SUBCASE("NaN and Inf propagate per candidate row") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        const py::object result = dtw_distance_batch(
            make_array({0.0}), make_matrix(2, 1, {nan, inf}), 0, 0);
        const auto out = py::reinterpret_borrow<ArrD>(result).unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(std::isnan(out(0)));
        CHECK(std::isinf(out(1)));
    }

    SUBCASE("very large and very small candidates match scalar policy") {
        const py::object large_result = dtw_distance_batch(
            make_array({1e150}), make_matrix(1, 1, {-1e150}), 0, 0);
        const auto large = py::reinterpret_borrow<ArrD>(large_result).unchecked<1>();
        CHECK(large(0) == doctest::Approx(1e150).epsilon(1e-12));

        const py::object small_result = dtw_distance_batch(
            make_array({1e-150}), make_matrix(1, 1, {-1e-150}), 0, 0);
        const auto small = py::reinterpret_borrow<ArrD>(small_result).unchecked<1>();
        CHECK(small(0) / 1e-150 == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known candidate distances are zero and one quarter") {
        const py::object result = dtw_distance_batch(
            make_array({0.0, 1.0}),
            make_matrix(2, 2, {0.0, 1.0, 0.0, 2.0}),
            0,
            0);
        const auto out = py::reinterpret_borrow<ArrD>(result).unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(0.0));
        CHECK(out(1) == doctest::Approx(0.25).epsilon(1e-12));
    }

    SUBCASE("Top-K breaks equal-distance ties by candidate index") {
        const py::object result = dtw_distance_batch(
            make_array({0.0, 1.0}),
            make_matrix(3, 2, {0.0, 1.0, 0.0, 1.0, 1.0, 1.0}),
            0,
            2);
        REQUIRE(py::isinstance<py::tuple>(result));
        const py::tuple top = py::reinterpret_borrow<py::tuple>(result);
        const auto indices = top[0].cast<ArrI64>().unchecked<1>();
        const auto distances = top[1].cast<ArrD>().unchecked<1>();
        REQUIRE(indices.shape(0) == 2);
        CHECK(indices(0) == 0);
        CHECK(indices(1) == 1);
        CHECK(distances(0) == doctest::Approx(0.0));
        CHECK(distances(1) == doctest::Approx(0.0));
    }

    SUBCASE("batch mode observes the same boundary window behavior") {
        const ArrD query = make_array({0.0, 1.0, 1.0});
        const ArrD candidates = make_matrix(1, 3, {0.0, 0.0, 1.0});
        const py::object diagonal_result = dtw_distance_batch(query, candidates, 0, 0);
        const py::object warped_result = dtw_distance_batch(query, candidates, 1, 0);
        const auto diagonal = py::reinterpret_borrow<ArrD>(diagonal_result).unchecked<1>();
        const auto warped = py::reinterpret_borrow<ArrD>(warped_result).unchecked<1>();
        CHECK(diagonal(0) == doctest::Approx(1.0 / 6.0).epsilon(1e-12));
        CHECK(warped(0) == doctest::Approx(0.0));
    }
}

TEST_CASE("compute_adx covers neutral, propagation, extremes, and known answers") {
    SUBCASE("empty input returns the neutral ADX value") {
        CHECK(compute_adx(make_array({}), make_array({}), make_array({}), 14)
              == doctest::Approx(25.0));
    }

    SUBCASE("a single OHLC point also returns the neutral ADX value") {
        CHECK(compute_adx(make_array({10.0}), make_array({9.0}), make_array({9.5}), 14)
              == doctest::Approx(25.0));
    }

    SUBCASE("NaN and Inf propagate to NaN for a full calculation window") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        OhlcVectors nan_data = make_trending_ohlc(1.0);
        nan_data.high[1] = nan;
        CHECK(std::isnan(compute_adx(
            make_array(nan_data.high), make_array(nan_data.low), make_array(nan_data.close), 2)));

        OhlcVectors inf_data = make_trending_ohlc(1.0);
        inf_data.high[1] = inf;
        CHECK(std::isnan(compute_adx(
            make_array(inf_data.high), make_array(inf_data.low), make_array(inf_data.close), 2)));
    }

    SUBCASE("very large trend approaches one hundred without overflow") {
        const OhlcVectors data = make_trending_ohlc(std::ldexp(1.0, 900));
        const double result = compute_adx(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        CHECK(std::isfinite(result));
        CHECK(result == doctest::Approx(100.0).epsilon(1e-12));
    }

    SUBCASE("very small trend is dominated by the fixed epsilon but remains finite") {
        const OhlcVectors data = make_trending_ohlc(std::ldexp(1.0, -900));
        const double result = compute_adx(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        CHECK(std::isfinite(result));
        CHECK(result >= 0.0);
        CHECK(result < 1e-200);
    }

    SUBCASE("flat prices have known ADX zero") {
        const std::vector<double> flat(18, 10.0);
        CHECK(compute_adx(make_array(flat), make_array(flat), make_array(flat), 2)
              == doctest::Approx(0.0));
    }
}

TEST_CASE("compute_atr covers short inputs, propagation, scaling, and a known series") {
    SUBCASE("empty input returns an empty array") {
        const ArrD result = compute_atr(make_array({}), make_array({}), make_array({}), 14);
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("a single point returns one NaN because the warmup is incomplete") {
        const ArrD result = compute_atr(
            make_array({10.0}), make_array({9.0}), make_array({9.5}), 14);
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 1);
        CHECK(std::isnan(out(0)));
    }

    SUBCASE("NaN propagates and Inf is preserved by Wilder smoothing") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        OhlcVectors nan_data = make_known_atr_input();
        nan_data.high[2] = nan;
        const auto nan_out = compute_atr(
            make_array(nan_data.high), make_array(nan_data.low), make_array(nan_data.close), 2)
                                 .unchecked<1>();
        CHECK(std::isnan(nan_out(2)));
        CHECK(std::isnan(nan_out(3)));

        OhlcVectors inf_data = make_known_atr_input();
        inf_data.high[2] = inf;
        const auto inf_out = compute_atr(
            make_array(inf_data.high), make_array(inf_data.low), make_array(inf_data.close), 2)
                                 .unchecked<1>();
        CHECK(std::isinf(inf_out(2)));
        CHECK(std::isinf(inf_out(3)));
    }

    SUBCASE("very large and very small finite inputs scale linearly") {
        for (const double scale : {std::ldexp(1.0, 900), std::ldexp(1.0, -900)}) {
            CAPTURE(scale);
            const OhlcVectors data = make_known_atr_input(scale);
            const auto out = compute_atr(
                make_array(data.high), make_array(data.low), make_array(data.close), 2)
                                 .unchecked<1>();
            CHECK(out(2) / scale == doctest::Approx(2.5).epsilon(1e-12));
            CHECK(out(3) / scale == doctest::Approx(2.75).epsilon(1e-12));
        }
    }

    SUBCASE("known ATR is NaN, NaN, 2.5, 2.75") {
        const OhlcVectors data = make_known_atr_input();
        const ArrD result = compute_atr(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 4);
        CHECK(std::isnan(out(0)));
        CHECK(std::isnan(out(1)));
        CHECK(out(2) == doctest::Approx(2.5).epsilon(1e-12));
        CHECK(out(3) == doctest::Approx(2.75).epsilon(1e-12));
    }
}

TEST_CASE("pattern_match_single covers invalid indices and deterministic features") {
    SUBCASE("empty prices reject T_idx as out of range without a native crash") {
        CHECK_THROWS_AS(run_pattern_single({}, 0), std::out_of_range);
    }

    SUBCASE("one price is valid input but has insufficient history and returns None") {
        const py::object result = run_pattern_single({1.0}, 0);
        CHECK(result.is_none());
    }

    SUBCASE("negative and one-past-end T_idx are rejected") {
        const std::vector<double> prices = {1.0, 2.0, 4.0};
        CHECK_THROWS_AS(run_pattern_single(prices, -1), std::out_of_range);
        CHECK_THROWS_AS(run_pattern_single(prices, 3), std::out_of_range);
    }

    SUBCASE("NaN and Inf in the query window are rejected as None") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        std::vector<double> nan_prices = make_periodic_prices(1.0);
        nan_prices[kPatternTIdx] = nan;
        CHECK(run_pattern_single(nan_prices).is_none());

        std::vector<double> inf_prices = make_periodic_prices(1.0);
        inf_prices[kPatternTIdx] = inf;
        CHECK(run_pattern_single(inf_prices).is_none());
    }

    SUBCASE("very large powers of two preserve the deterministic known features") {
        const py::object result = run_pattern_single(
            make_periodic_prices(std::ldexp(1.0, 900)));
        REQUIRE_FALSE(result.is_none());
        REQUIRE(py::isinstance<py::dict>(result));
        check_periodic_expected_features(
            values_from_dict(py::reinterpret_borrow<py::dict>(result)));
    }

    SUBCASE("very small prices are floored, lose shape, and return None") {
        const py::object result = run_pattern_single(
            make_periodic_prices(std::ldexp(1.0, -900)));
        CHECK(result.is_none());
    }

    SUBCASE("periodic prices have a hand-derived 15-feature answer") {
        const py::object result = run_pattern_single(make_periodic_prices(1.0));
        REQUIRE_FALSE(result.is_none());
        REQUIRE(py::isinstance<py::dict>(result));
        check_periodic_expected_features(
            values_from_dict(py::reinterpret_borrow<py::dict>(result)));
    }
}

TEST_CASE("pattern_match_batch covers masks, extremes, and deterministic features") {
    SUBCASE("empty prices and indices return shapes zero by fifteen and zero") {
        const py::tuple result = run_pattern_batch({}, {});
        const ArrD features = result[0].cast<ArrD>();
        const py::array_t<bool> mask = result[1].cast<py::array_t<bool>>();
        CHECK(features.ndim() == 2);
        CHECK(features.shape(0) == 0);
        CHECK(features.shape(1) == 15);
        CHECK(mask.shape(0) == 0);
    }

    SUBCASE("one price yields no feature row and a false validity mask") {
        const py::tuple result = run_pattern_batch({1.0}, {0});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        CHECK(features.shape(0) == 0);
        REQUIRE(mask.shape(0) == 1);
        CHECK_FALSE(mask(0));
    }

    SUBCASE("NaN and Inf in the query window produce false masks") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        for (const double bad_value : {nan, inf}) {
            std::vector<double> prices = make_periodic_prices(1.0);
            prices[kPatternTIdx] = bad_value;
            const py::tuple result = run_pattern_batch(prices, {kPatternTIdx});
            const ArrD features = result[0].cast<ArrD>();
            const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
            CHECK(features.shape(0) == 0);
            REQUIRE(mask.shape(0) == 1);
            CHECK_FALSE(mask(0));
        }
    }

    SUBCASE("very large powers of two preserve one known feature row") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(std::ldexp(1.0, 900)), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        REQUIRE(features.shape(0) == 1);
        REQUIRE(features.shape(1) == 15);
        REQUIRE(mask.shape(0) == 1);
        CHECK(mask(0));
        check_periodic_expected_features(values_from_batch_row(features, 0));
    }

    SUBCASE("very small prices produce no feature rows and a false mask") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(std::ldexp(1.0, -900)), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        CHECK(features.shape(0) == 0);
        REQUIRE(mask.shape(0) == 1);
        CHECK_FALSE(mask(0));
    }

    SUBCASE("periodic prices have the same hand-derived feature row as single mode") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(1.0), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        REQUIRE(features.shape(0) == 1);
        REQUIRE(features.shape(1) == 15);
        REQUIRE(mask.shape(0) == 1);
        CHECK(mask(0));
        check_periodic_expected_features(values_from_batch_row(features, 0));
    }
}
"""; Path("tests/test_etf_core.cpp").write_bytes(content.replace("'"\\n\", \"\\r\\n\").encode(\"utf-8\"))'" in E:\workspace\projects\形态匹配ETF策略-pybind11
2026-07-17T09:57:21.095420Z ERROR codex_core::tools::router: error=Exit code: 1
Wall time: 0.2 seconds
Output:
  File "<string>", line 1
    from pathlib import Path; content = r"/**
                                        ^
SyntaxError: unterminated string literal (detected at line 1)

 exited 1 in 160ms:
  File "<string>", line 1
    from pathlib import Path; content = r"/**
                                        ^
SyntaxError: unterminated string literal (detected at line 1)

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $content = @'"'
/**
 * test_etf_core.cpp — etf_core 原生 C++ 算法测试
 *
 * 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17
 */

#define DOCTEST_CONFIG_IMPLEMENT
#include <doctest/doctest.h>

#include <pybind11/embed.h>
#include <pybind11/numpy.h>

#include <array>
#include <cmath>
#include <cstdint>
#include <limits>
#include <stdexcept>
#include <vector>

namespace py = pybind11;

using ArrD = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;

// etf_core.cpp 当前没有公共 C++ 头文件，因此在此声明原生入口。
// 测试直接调用这些符号，不导入 Python 扩展模块，也不测试绑定分发层。
ArrD standardize_returns(ArrD price_series);
double cosine_similarity(ArrD x_arr, ArrD y_arr);
double dtw_distance(ArrD x_arr, ArrD y_arr, int window);
py::object dtw_distance_batch(ArrD query_arr, ArrD candidates_arr, int window, int top_k);
double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
py::object pattern_match_single(
    ArrD prices_arr,
    int T_idx,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);
py::tuple pattern_match_batch(
    ArrD prices_arr,
    ArrI64 t_indices_arr,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);

// 非有限值策略（由 etf_core.cpp 的当前实现定义）：
// 1. standardize_returns 对价格窗口执行有限性检查；任一 NaN/Inf 都拒绝整个窗口并返回空数组。
// 2. cosine_similarity 与 DTW 不预先拒绝 NaN/Inf，而是按 IEEE-754 传播；Inf/Inf 等不定式产生 NaN。
// 3. compute_adx 与 compute_atr 不预先拒绝 NaN/Inf；ADX 中 Inf/Inf 可变为 NaN，ATR 保留 NaN/Inf。
// 4. pattern_match_single/batch 通过标准化步骤拒绝含 NaN/Inf 的查询窗口；single 返回 None，batch 标记无效。

namespace {

constexpr int kPatternTIdx = 30;
constexpr int kPatternK = 50;
constexpr int kPatternQueryLength = 3;
constexpr int kPatternLookback = 100;
constexpr int kPatternStep = 1;
constexpr int kPatternForward = 1;
constexpr int kPatternDtwWindow = 1;
constexpr int kPatternPrefilterTop = 50;

constexpr std::array<const char*, 15> kFeatureKeys = {
    \"top1_sim\",
    \"top5_avg_sim\",
    \"sim_decay\",
    \"sim_variance\",
    \"match_distance_ratio\",
    \"avg_future_ret\",
    \"weighted_future_ret\",
    \"median_future_ret\",
    \"ret_sign_consistency\",
    \"best_match_ret\",
    \"max_dd_in_matches\",
    \"match_time_span\",
    \"match_time_span_ratio\",
    \"match_cluster_ratio\",
    \"n_matches_above_thresh\",
};

constexpr std::array<double, 15> kPeriodicExpectedFeatures = {
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    0.0,
    24.0,
    0.24,
    1.0,
    0.0,
};

ArrD make_array(const std::vector<double>& values) {
    ArrD result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_array(std::initializer_list<double> values) {
    return make_array(std::vector<double>(values));
}

ArrI64 make_index_array(const std::vector<int64_t>& values) {
    ArrI64 result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    const std::vector<double>& values) {
    if (values.size() "'!= static_cast<std::size_t>(rows * cols)) {
        throw std::invalid_argument("matrix data size does not match shape");
    }

    ArrD result(std::vector<py::ssize_t>{rows, cols});
    auto out = result.mutable_unchecked<2>();
    for (py::ssize_t row = 0; row < rows; ++row) {
        for (py::ssize_t col = 0; col < cols; ++col) {
            out(row, col) = values[static_cast<std::size_t>(row * cols + col)];
        }
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    std::initializer_list<double> values) {
    return make_matrix(rows, cols, std::vector<double>(values));
}

std::vector<double> make_periodic_prices(double scale) {
    std::vector<double> prices(41);
    prices[0] = scale;
    for (std::size_t i = 1; i < prices.size(); ++i) {
        const double factor = ((i - 1) % 2 == 0) ? 2.0 : 4.0;
        prices[i] = prices[i - 1] * factor;
    }
    return prices;
}

struct OhlcVectors {
    std::vector<double> high;
    std::vector<double> low;
    std::vector<double> close;
};

OhlcVectors make_trending_ohlc(double scale) {
    OhlcVectors data;
    data.high.resize(18);
    data.low.resize(18);
    data.close.resize(18);

    for (std::size_t i = 0; i < data.close.size(); ++i) {
        data.close[i] = (static_cast<double>(i) + 2.0) * scale;
        data.high[i] = data.close[i] + 0.5 * scale;
        data.low[i] = data.close[i] - 0.5 * scale;
    }
    return data;
}

OhlcVectors make_known_atr_input(double scale = 1.0) {
    return {
        {10.0 * scale, 12.0 * scale, 13.0 * scale, 15.0 * scale},
        {8.0 * scale, 9.0 * scale, 11.0 * scale, 12.0 * scale},
        {9.0 * scale, 11.0 * scale, 12.0 * scale, 14.0 * scale},
    };
}

py::object run_pattern_single(const std::vector<double>& prices, int t_idx = kPatternTIdx) {
    return pattern_match_single(
        make_array(prices),
        t_idx,
        kPatternK,
        kPatternQueryLength,
        kPatternLookback,
        kPatternStep,
        kPatternForward,
        kPatternDtwWindow,
        kPatternPrefilterTop);
}

py::tuple run_pattern_batch(
    const std::vector<double>& prices,
    const std::vector<int64_t>& t_indices) {
    return pattern_match_batch(
        make_array(prices),
        make_index_array(t_indices),
        kPatternK,
        kPatternQueryLength,
        kPatternLookback,
        kPatternStep,
        kPatternForward,
        kPatternDtwWindow,
        kPatternPrefilterTop);
}

std::array<double, 15> values_from_dict(const py::dict& result) {
    std::array<double, 15> values{};
    for (std::size_t i = 0; i < kFeatureKeys.size(); ++i) {
        values[i] = py::cast<double>(result[py::str(kFeatureKeys[i])]);
    }
    return values;
}

std::array<double, 15> values_from_batch_row(const ArrD& features, py::ssize_t row) {
    const auto data = features.unchecked<2>();
    std::array<double, 15> values{};
    for (py::ssize_t col = 0; col < 15; ++col) {
        values[static_cast<std::size_t>(col)] = data(row, col);
    }
    return values;
}

void check_periodic_expected_features(const std::array<double, 15>& actual) {
    for (std::size_t i = 0; i < actual.size(); ++i) {
        CAPTURE(i);
        CHECK(actual[i] == doctest::Approx(kPeriodicExpectedFeatures[i]).epsilon(1e-12));
    }
}

} // namespace

int main(int argc, char** argv) {
    py::scoped_interpreter interpreter{};
    doctest::Context context(argc, argv);
    return context.run();
}

TEST_CASE("standardize_returns covers edge cases and a hand-computed result") {
    SUBCASE("empty input returns an empty array") {
        const ArrD result = standardize_returns(make_array({}));
        CHECK(result.ndim() == 1);
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("single price returns an empty array") {
        const ArrD result = standardize_returns(make_array({42.0}));
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("NaN and Inf reject the whole price window") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(standardize_returns(make_array({1.0, nan, 2.0})).shape(0) == 0);
        CHECK(standardize_returns(make_array({1.0, inf, 2.0})).shape(0) == 0);
    }

    SUBCASE("very small prices are floored and become zero returns") {
        const double tiny = std::ldexp(1.0, -900);
        const ArrD result = standardize_returns(make_array({tiny, 2.0 * tiny, 8.0 * tiny}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(0.0));
        CHECK(out(1) == doctest::Approx(0.0));
    }

    SUBCASE("very large finite prices remain numerically stable") {
        const double huge = std::ldexp(1.0, 900);
        const ArrD result = standardize_returns(make_array({huge, 2.0 * huge, 8.0 * huge}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(-1.0).epsilon(1e-12));
        CHECK(out(1) == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known answer for prices 1, 2, 8 is -1, 1") {
        const ArrD result = standardize_returns(make_array({1.0, 2.0, 8.0}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(-1.0).epsilon(1e-12));
        CHECK(out(1) == doctest::Approx(1.0).epsilon(1e-12));
    }
}

TEST_CASE("cosine_similarity covers edge cases and a hand-computed result") {
    SUBCASE("empty vectors return the neutral similarity zero") {
        CHECK(cosine_similarity(make_array({}), make_array({})) == doctest::Approx(0.0));
    }

    SUBCASE("single positive elements have similarity one") {
        CHECK(cosine_similarity(make_array({2.0}), make_array({3.0})) == doctest::Approx(1.0));
    }

    SUBCASE("NaN and Inf propagate to NaN") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(std::isnan(cosine_similarity(make_array({nan}), make_array({1.0}))));
        CHECK(std::isnan(cosine_similarity(make_array({inf}), make_array({1.0}))));
    }

    SUBCASE("very small norm returns zero and huge squaring overflow returns NaN") {
        CHECK(cosine_similarity(make_array({1e-300}), make_array({1.0})) == doctest::Approx(0.0));
        CHECK(std::isnan(cosine_similarity(make_array({1e308}), make_array({1e308}))));
    }

    SUBCASE("known answer is four fifths") {
        CHECK(cosine_similarity(make_array({1.0, 2.0}), make_array({2.0, 1.0}))
              == doctest::Approx(0.8).epsilon(1e-12));
    }

    SUBCASE("mismatched lengths are rejected") {
        CHECK_THROWS_AS(
            cosine_similarity(make_array({1.0}), make_array({1.0, 2.0})),
            std::invalid_argument);
    }
}

TEST_CASE("dtw_distance covers ties, window boundaries, and numeric policies") {
    SUBCASE("an empty sequence returns infinity") {
        CHECK(std::isinf(dtw_distance(make_array({}), make_array({1.0}), 1)));
        CHECK(std::isinf(dtw_distance(make_array({1.0}), make_array({}), 1)));
    }

    SUBCASE("single elements use sqrt squared cost divided by total length") {
        CHECK(dtw_distance(make_array({2.0}), make_array({5.0}), 0)
              == doctest::Approx(1.5).epsilon(1e-12));
    }

    SUBCASE("NaN propagates and finite versus Inf returns Inf") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(std::isnan(dtw_distance(make_array({nan}), make_array({0.0}), 0)));
        CHECK(std::isinf(dtw_distance(make_array({inf}), make_array({0.0}), 0)));
    }

    SUBCASE("very large and very small finite costs remain representable") {
        CHECK(dtw_distance(make_array({1e150}), make_array({-1e150}), 0)
              == doctest::Approx(1e150).epsilon(1e-12));
        CHECK(dtw_distance(make_array({1e-150}), make_array({-1e-150}), 0) / 1e-150
              == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known diagonal answer is one quarter") {
        CHECK(dtw_distance(make_array({0.0, 1.0}), make_array({0.0, 2.0}), 0)
              == doctest::Approx(0.25).epsilon(1e-12));
    }

    SUBCASE("equal predecessor ties stay deterministic in distance") {
        CHECK(dtw_distance(make_array({0.0, 0.0}), make_array({0.0, 0.0, 0.0}), 0)
              == doctest::Approx(0.0));
    }

    SUBCASE("window zero enforces the diagonal and window one permits warping") {
        const ArrD x = make_array({0.0, 1.0, 1.0});
        const ArrD y = make_array({0.0, 0.0, 1.0});
        CHECK(dtw_distance(x, y, 0) == doctest::Approx(1.0 / 6.0).epsilon(1e-12));
        CHECK(dtw_distance(x, y, 1) == doctest::Approx(0.0));
    }
}

TEST_CASE("dtw_distance_batch matches scalar DTW and honors Top-K ties") {
    SUBCASE("empty candidates return empty arrays in both modes") {
        const py::object all_result = dtw_distance_batch(
            make_array({}), make_matrix(0, 0, {}), 0, 0);
        const ArrD all_distances = py::reinterpret_borrow<ArrD>(all_result);
        CHECK(all_distances.shape(0) == 0);

        const py::object top_result = dtw_distance_batch(
            make_array({}), make_matrix(0, 0, {}), 0, 1);
        REQUIRE(py::isinstance<py::tuple>(top_result));
        const py::tuple top = py::reinterpret_borrow<py::tuple>(top_result);
        const ArrI64 indices = top[0].cast<ArrI64>();
        const ArrD distances = top[1].cast<ArrD>();
        CHECK(indices.shape(0) == 0);
        CHECK(distances.shape(0) == 0);
    }

    SUBCASE("one query value and one candidate produce the scalar answer") {
        const py::object result = dtw_distance_batch(
            make_array({2.0}), make_matrix(1, 1, {5.0}), 0, 0);
        const ArrD distances = py::reinterpret_borrow<ArrD>(result);
        const auto out = distances.unchecked<1>();
        REQUIRE(out.shape(0) == 1);
        CHECK(out(0) == doctest::Approx(1.5).epsilon(1e-12));
    }

    SUBCASE("NaN and Inf propagate per candidate row") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        const py::object result = dtw_distance_batch(
            make_array({0.0}), make_matrix(2, 1, {nan, inf}), 0, 0);
        const auto out = py::reinterpret_borrow<ArrD>(result).unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(std::isnan(out(0)));
        CHECK(std::isinf(out(1)));
    }

    SUBCASE("very large and very small candidates match scalar policy") {
        const py::object large_result = dtw_distance_batch(
            make_array({1e150}), make_matrix(1, 1, {-1e150}), 0, 0);
        const auto large = py::reinterpret_borrow<ArrD>(large_result).unchecked<1>();
        CHECK(large(0) == doctest::Approx(1e150).epsilon(1e-12));

        const py::object small_result = dtw_distance_batch(
            make_array({1e-150}), make_matrix(1, 1, {-1e-150}), 0, 0);
        const auto small = py::reinterpret_borrow<ArrD>(small_result).unchecked<1>();
        CHECK(small(0) / 1e-150 == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known candidate distances are zero and one quarter") {
        const py::object result = dtw_distance_batch(
            make_array({0.0, 1.0}),
            make_matrix(2, 2, {0.0, 1.0, 0.0, 2.0}),
            0,
            0);
        const auto out = py::reinterpret_borrow<ArrD>(result).unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(0.0));
        CHECK(out(1) == doctest::Approx(0.25).epsilon(1e-12));
    }

    SUBCASE("Top-K breaks equal-distance ties by candidate index") {
        const py::object result = dtw_distance_batch(
            make_array({0.0, 1.0}),
            make_matrix(3, 2, {0.0, 1.0, 0.0, 1.0, 1.0, 1.0}),
            0,
            2);
        REQUIRE(py::isinstance<py::tuple>(result));
        const py::tuple top = py::reinterpret_borrow<py::tuple>(result);
        const auto indices = top[0].cast<ArrI64>().unchecked<1>();
        const auto distances = top[1].cast<ArrD>().unchecked<1>();
        REQUIRE(indices.shape(0) == 2);
        CHECK(indices(0) == 0);
        CHECK(indices(1) == 1);
        CHECK(distances(0) == doctest::Approx(0.0));
        CHECK(distances(1) == doctest::Approx(0.0));
    }

    SUBCASE("batch mode observes the same boundary window behavior") {
        const ArrD query = make_array({0.0, 1.0, 1.0});
        const ArrD candidates = make_matrix(1, 3, {0.0, 0.0, 1.0});
        const py::object diagonal_result = dtw_distance_batch(query, candidates, 0, 0);
        const py::object warped_result = dtw_distance_batch(query, candidates, 1, 0);
        const auto diagonal = py::reinterpret_borrow<ArrD>(diagonal_result).unchecked<1>();
        const auto warped = py::reinterpret_borrow<ArrD>(warped_result).unchecked<1>();
        CHECK(diagonal(0) == doctest::Approx(1.0 / 6.0).epsilon(1e-12));
        CHECK(warped(0) == doctest::Approx(0.0));
    }
}

TEST_CASE("compute_adx covers neutral, propagation, extremes, and known answers") {
    SUBCASE("empty input returns the neutral ADX value") {
        CHECK(compute_adx(make_array({}), make_array({}), make_array({}), 14)
              == doctest::Approx(25.0));
    }

    SUBCASE("a single OHLC point also returns the neutral ADX value") {
        CHECK(compute_adx(make_array({10.0}), make_array({9.0}), make_array({9.5}), 14)
              == doctest::Approx(25.0));
    }

    SUBCASE("NaN and Inf propagate to NaN for a full calculation window") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        OhlcVectors nan_data = make_trending_ohlc(1.0);
        nan_data.high[1] = nan;
        CHECK(std::isnan(compute_adx(
            make_array(nan_data.high), make_array(nan_data.low), make_array(nan_data.close), 2)));

        OhlcVectors inf_data = make_trending_ohlc(1.0);
        inf_data.high[1] = inf;
        CHECK(std::isnan(compute_adx(
            make_array(inf_data.high), make_array(inf_data.low), make_array(inf_data.close), 2)));
    }

    SUBCASE("very large trend approaches one hundred without overflow") {
        const OhlcVectors data = make_trending_ohlc(std::ldexp(1.0, 900));
        const double result = compute_adx(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        CHECK(std::isfinite(result));
        CHECK(result == doctest::Approx(100.0).epsilon(1e-12));
    }

    SUBCASE("very small trend is dominated by the fixed epsilon but remains finite") {
        const OhlcVectors data = make_trending_ohlc(std::ldexp(1.0, -900));
        const double result = compute_adx(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        CHECK(std::isfinite(result));
        CHECK(result >= 0.0);
        CHECK(result < 1e-200);
    }

    SUBCASE("flat prices have known ADX zero") {
        const std::vector<double> flat(18, 10.0);
        CHECK(compute_adx(make_array(flat), make_array(flat), make_array(flat), 2)
              == doctest::Approx(0.0));
    }
}

TEST_CASE("compute_atr covers short inputs, propagation, scaling, and a known series") {
    SUBCASE("empty input returns an empty array") {
        const ArrD result = compute_atr(make_array({}), make_array({}), make_array({}), 14);
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("a single point returns one NaN because the warmup is incomplete") {
        const ArrD result = compute_atr(
            make_array({10.0}), make_array({9.0}), make_array({9.5}), 14);
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 1);
        CHECK(std::isnan(out(0)));
    }

    SUBCASE("NaN propagates and Inf is preserved by Wilder smoothing") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        OhlcVectors nan_data = make_known_atr_input();
        nan_data.high[2] = nan;
        const auto nan_out = compute_atr(
            make_array(nan_data.high), make_array(nan_data.low), make_array(nan_data.close), 2)
                                 .unchecked<1>();
        CHECK(std::isnan(nan_out(2)));
        CHECK(std::isnan(nan_out(3)));

        OhlcVectors inf_data = make_known_atr_input();
        inf_data.high[2] = inf;
        const auto inf_out = compute_atr(
            make_array(inf_data.high), make_array(inf_data.low), make_array(inf_data.close), 2)
                                 .unchecked<1>();
        CHECK(std::isinf(inf_out(2)));
        CHECK(std::isinf(inf_out(3)));
    }

    SUBCASE("very large and very small finite inputs scale linearly") {
        for (const double scale : {std::ldexp(1.0, 900), std::ldexp(1.0, -900)}) {
            CAPTURE(scale);
            const OhlcVectors data = make_known_atr_input(scale);
            const auto out = compute_atr(
                make_array(data.high), make_array(data.low), make_array(data.close), 2)
                                 .unchecked<1>();
            CHECK(out(2) / scale == doctest::Approx(2.5).epsilon(1e-12));
            CHECK(out(3) / scale == doctest::Approx(2.75).epsilon(1e-12));
        }
    }

    SUBCASE("known ATR is NaN, NaN, 2.5, 2.75") {
        const OhlcVectors data = make_known_atr_input();
        const ArrD result = compute_atr(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 4);
        CHECK(std::isnan(out(0)));
        CHECK(std::isnan(out(1)));
        CHECK(out(2) == doctest::Approx(2.5).epsilon(1e-12));
        CHECK(out(3) == doctest::Approx(2.75).epsilon(1e-12));
    }
}

TEST_CASE("pattern_match_single covers invalid indices and deterministic features") {
    SUBCASE("empty prices reject T_idx as out of range without a native crash") {
        CHECK_THROWS_AS(run_pattern_single({}, 0), std::out_of_range);
    }

    SUBCASE("one price is valid input but has insufficient history and returns None") {
        const py::object result = run_pattern_single({1.0}, 0);
        CHECK(result.is_none());
    }

    SUBCASE("negative and one-past-end T_idx are rejected") {
        const std::vector<double> prices = {1.0, 2.0, 4.0};
        CHECK_THROWS_AS(run_pattern_single(prices, -1), std::out_of_range);
        CHECK_THROWS_AS(run_pattern_single(prices, 3), std::out_of_range);
    }

    SUBCASE("NaN and Inf in the query window are rejected as None") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        std::vector<double> nan_prices = make_periodic_prices(1.0);
        nan_prices[kPatternTIdx] = nan;
        CHECK(run_pattern_single(nan_prices).is_none());

        std::vector<double> inf_prices = make_periodic_prices(1.0);
        inf_prices[kPatternTIdx] = inf;
        CHECK(run_pattern_single(inf_prices).is_none());
    }

    SUBCASE("very large powers of two preserve the deterministic known features") {
        const py::object result = run_pattern_single(
            make_periodic_prices(std::ldexp(1.0, 900)));
        REQUIRE_FALSE(result.is_none());
        REQUIRE(py::isinstance<py::dict>(result));
        check_periodic_expected_features(
            values_from_dict(py::reinterpret_borrow<py::dict>(result)));
    }

    SUBCASE("very small prices are floored, lose shape, and return None") {
        const py::object result = run_pattern_single(
            make_periodic_prices(std::ldexp(1.0, -900)));
        CHECK(result.is_none());
    }

    SUBCASE("periodic prices have a hand-derived 15-feature answer") {
        const py::object result = run_pattern_single(make_periodic_prices(1.0));
        REQUIRE_FALSE(result.is_none());
        REQUIRE(py::isinstance<py::dict>(result));
        check_periodic_expected_features(
            values_from_dict(py::reinterpret_borrow<py::dict>(result)));
    }
}

TEST_CASE("pattern_match_batch covers masks, extremes, and deterministic features") {
    SUBCASE("empty prices and indices return shapes zero by fifteen and zero") {
        const py::tuple result = run_pattern_batch({}, {});
        const ArrD features = result[0].cast<ArrD>();
        const py::array_t<bool> mask = result[1].cast<py::array_t<bool>>();
        CHECK(features.ndim() == 2);
        CHECK(features.shape(0) == 0);
        CHECK(features.shape(1) == 15);
        CHECK(mask.shape(0) == 0);
    }

    SUBCASE("one price yields no feature row and a false validity mask") {
        const py::tuple result = run_pattern_batch({1.0}, {0});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        CHECK(features.shape(0) == 0);
        REQUIRE(mask.shape(0) == 1);
        CHECK_FALSE(mask(0));
    }

    SUBCASE("NaN and Inf in the query window produce false masks") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        for (const double bad_value : {nan, inf}) {
            std::vector<double> prices = make_periodic_prices(1.0);
            prices[kPatternTIdx] = bad_value;
            const py::tuple result = run_pattern_batch(prices, {kPatternTIdx});
            const ArrD features = result[0].cast<ArrD>();
            const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
            CHECK(features.shape(0) == 0);
            REQUIRE(mask.shape(0) == 1);
            CHECK_FALSE(mask(0));
        }
    }

    SUBCASE("very large powers of two preserve one known feature row") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(std::ldexp(1.0, 900)), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        REQUIRE(features.shape(0) == 1);
        REQUIRE(features.shape(1) == 15);
        REQUIRE(mask.shape(0) == 1);
        CHECK(mask(0));
        check_periodic_expected_features(values_from_batch_row(features, 0));
    }

    SUBCASE("very small prices produce no feature rows and a false mask") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(std::ldexp(1.0, -900)), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        CHECK(features.shape(0) == 0);
        REQUIRE(mask.shape(0) == 1);
        CHECK_FALSE(mask(0));
    }

    SUBCASE("periodic prices have the same hand-derived feature row as single mode") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(1.0), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        REQUIRE(features.shape(0) == 1);
        REQUIRE(features.shape(1) == 15);
        REQUIRE(mask.shape(0) == 1);
        CHECK(mask(0));
        check_periodic_expected_features(values_from_batch_row(features, 0));
    }
}
'"'@; "'$content = $content -replace "`r?`n", "`r`n"; [System.IO.File]::WriteAllText((Join-Path (Get-Location) '"'tests/test_etf_core.cpp'), "'$content, [System.Text.UTF8Encoding]::new($false))' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 151ms:
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $content = @'"'
cmake_minimum_required(VERSION 3.20)

# etf_core 原生 C++ 测试
# 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17

if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    project(etf_core_native_tests LANGUAGES CXX)
endif()

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# 测试直接调用含 py::array_t 参数的 C++ 入口，因此需要嵌入式 Python 运行时。
set(Python_EXECUTABLE \"\" CACHE FILEPATH \"Path to python.exe\")
if(Python_EXECUTABLE)
    get_filename_component(Python_ROOT_DIR \""'${Python_EXECUTABLE}" DIRECTORY)
endif()
find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Embed)

# pybind11 — 与项目根 CMakeLists.txt 使用相同的自动探测策略。
set(pybind11_DIR "" CACHE PATH "pybind11 cmake config dir")
if(NOT pybind11_DIR)
    execute_process(
        COMMAND "${Python_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE _pybind11_cmake_dir
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )
    if(_pybind11_cmake_dir)
        set(pybind11_DIR "${_pybind11_cmake_dir}")
    endif()
endif()
if(NOT pybind11_DIR)
    message(FATAL_ERROR
        "pybind11 not found. Install it for the selected Python or set pybind11_DIR.")
endif()
find_package(pybind11 REQUIRED CONFIG)

include(FetchContent)
set(DOCTEST_WITH_TESTS OFF CACHE BOOL "" FORCE)
FetchContent_Declare(
    doctest
    GIT_REPOSITORY https://github.com/doctest/doctest.git
    GIT_TAG v2.4.11
    GIT_SHALLOW TRUE
)
FetchContent_MakeAvailable(doctest)

get_filename_component(ETF_PROJECT_ROOT "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)
set(ETF_CORE_SOURCE "${ETF_PROJECT_ROOT}/src/cpp/etf_core.cpp")

# 生产 target etf_core 是 MODULE_LIBRARY；CMake 禁止可执行文件直接链接 MODULE_LIBRARY。
# 独立配置 tests/ 时，使用同一生产源文件创建可链接的静态 etf_core；若未来从根工程
# add_subdirectory(tests)，则保留生产模块并创建仅供原生测试链接的 etf_core_native_link。
if(TARGET etf_core)
    get_target_property(_etf_core_type etf_core TYPE)
endif()

if(TARGET etf_core AND NOT _etf_core_type STREQUAL "MODULE_LIBRARY")
    set(ETF_CORE_NATIVE_TARGET etf_core)
elseif(TARGET etf_core)
    set(ETF_CORE_NATIVE_TARGET etf_core_native_link)
    if(NOT TARGET ${ETF_CORE_NATIVE_TARGET})
        add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
        target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
        target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
    endif()
else()
    set(ETF_CORE_NATIVE_TARGET etf_core)
    add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
    target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
    target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
endif()

add_executable(test_native test_etf_core.cpp)
target_compile_features(test_native PRIVATE cxx_std_20)
target_link_libraries(
    test_native
    PRIVATE
        doctest::doctest
        ${ETF_CORE_NATIVE_TARGET}
        pybind11::embed
)

if(MSVC)
    target_compile_options(test_native PRIVATE /utf-8 /wd4819)
    if(ETF_CORE_NATIVE_TARGET STREQUAL "etf_core_native_link"
       OR (ETF_CORE_NATIVE_TARGET STREQUAL "etf_core" AND NOT _etf_core_type))
        target_compile_options(${ETF_CORE_NATIVE_TARGET} PRIVATE /utf-8 /wd4819)
    endif()
endif()

enable_testing()
add_test(NAME test_native COMMAND test_native)
'"'@; "'$content = $content -replace "`r?`n", "`r`n"; [System.IO.File]::WriteAllText((Join-Path (Get-Location) '"'tests/CMakeLists.txt'), "'$content, [System.Text.UTF8Encoding]::new($false))' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 148ms:
已确认 8 个函数的签名、边界条件与非有限值行为，并完成两个新文件的初稿。下一步仅做静态复核，不配置、编译或运行测试。
  ✓ 检查现有 C++ 源码与 CMake 结构，确认函数签名和行为
  ✓ 编写 tests/test_etf_core.cpp，覆盖 8 个核心函数
  ✓ 编写 tests/CMakeLists.txt，配置 doctest 与原生测试目标
  → 静态复核编码、文件内容与 Git 变更（不编译、不运行测试）
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Output '"'--- tests/test_etf_core.cpp ---'; Get-Content -Raw -Encoding UTF8 'tests/test_etf_core.cpp'; Write-Output '--- tests/CMakeLists.txt ---'; Get-Content -Raw -Encoding UTF8 'tests/CMakeLists.txt'; Write-Output '--- encoding and line endings ---'; foreach ("'$path in @('"'tests/test_etf_core.cpp', 'tests/CMakeLists.txt')) { "'$bytes = [System.IO.File]::ReadAllBytes((Resolve-Path $path)); $hasBom = $bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF; $text = [System.Text.Encoding]::UTF8.GetString($bytes); $crlf = ([regex]::Matches($text, "`r`n")).Count; $bareLf = ([regex]::Matches($text, "(?<!`r)`n")).Count; Write-Output ("{0}: bytes={1}, UTF8_BOM={2}, CRLF={3}, bare_LF={4}" -f $path, $bytes.Length, $hasBom, $crlf, $bareLf) }; Write-Output '"'--- git diff --stat/status ---'; git status --short; git diff --stat -- tests/test_etf_core.cpp tests/CMakeLists.txt; git diff --no-index -- /dev/null tests/test_etf_core.cpp 2>"'$null | Select-Object -First 40; git diff --no-index -- /dev/null tests/CMakeLists.txt 2>$null' in E:\workspace\projects\形态匹配ETF策略-pybind11
2026-07-17T10:01:35.437026Z ERROR codex_core::tools::router: error=Exit code: 1
Wall time: 0.3 seconds
Total output lines: 955
Output:
--- tests/test_etf_core.cpp ---
/**
 * test_etf_core.cpp — etf_core 原生 C++ 算法测试
 *
 * 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17
 */

#define DOCTEST_CONFIG_IMPLEMENT
#include <doctest/doctest.h>

#include <pybind11/embed.h>
#include <pybind11/numpy.h>

#include <array>
#include <cmath>
#include <cstdint>
#include <limits>
#include <stdexcept>
#include <vector>

namespace py = pybind11;

using ArrD = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;

// etf_core.cpp 当前没有公共 C++ 头文件，因此在此声明原生入口。
// 测试直接调用这些符号，不导入 Python 扩展模块，也不测试绑定分发层。
ArrD standardize_returns(ArrD price_series);
double cosine_similarity(ArrD x_arr, ArrD y_arr);
double dtw_distance(ArrD x_arr, ArrD y_arr, int window);
py::object dtw_distance_batch(ArrD query_arr, ArrD candidates_arr, int window, int top_k);
double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
py::object pattern_match_single(
    ArrD prices_arr,
    int T_idx,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);
py::tuple pattern_match_batch(
    ArrD prices_arr,
    ArrI64 t_indices_arr,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);

// 非有限值策略（由 etf_core.cpp 的当前实现定义）：
// 1. standardize_returns 对价格窗口执行有限性检查；任一 NaN/Inf 都拒绝整个窗口并返回空数组。
// 2. cosine_similarity 与 DTW 不预先拒绝 NaN/Inf，而是按 IEEE-754 传播；Inf/Inf 等不定式产生 NaN。
// 3. compute_adx 与 compute_atr 不预先拒绝 NaN/Inf；ADX 中 Inf/Inf 可变为 NaN，ATR 保留 NaN/Inf。
// 4. pattern_match_single/batch 通过标准化步骤拒绝含 NaN/Inf 的查询窗口；single 返回 None，batch 标记无效。

namespace {

constexpr int kPatternTIdx = 30;
constexpr int kPatternK = 50;
constexpr int kPatternQueryLength = 3;
constexpr int kPatternLookback = 100;
constexpr int kPatternStep = 1;
constexpr int kPatternForward = 1;
constexpr int kPatternDtwWindow = 1;
constexpr int kPatternPrefilterTop = 50;

constexpr std::array<const char*, 15> kFeatureKeys = {
    "top1_sim",
    "top5_avg_sim",
    "sim_decay",
    "sim_variance",
    "match_distance_ratio",
    "avg_future_ret",
    "weighted_future_ret",
    "median_future_ret",
    "ret_sign_consistency",
    "best_match_ret",
    "max_dd_in_matches",
    "match_time_span",
    "match_time_span_ratio",
    "match_cluster_ratio",
    "n_matches_above_thresh",
};

constexpr std::array<double, 15> kPeriodicExpectedFeatures = {
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    0.0,
    24.0,
    0.24,
    1.0,
    0.0,
};

ArrD make_array(const std::vector<double>& values) {
    ArrD result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_array(std::initializer_list<double> values) {
    return make_array(std::vector<double>(values));
}

ArrI64 make_index_array(const std::vector<int64_t>& values) {
    ArrI64 result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    const std::vector<double>& values) {
    if (values.size() != static_cast<std::size_t>(rows * cols)) {
        throw std::invalid_argument("matrix data size does not match shape");
    }

    ArrD result(std::vector<py::ssize_t>{rows, cols});
    auto out = result.mutable_unchecked<2>();
    for (py::ssize_t row = 0; row < rows; ++row) {
        for (py::ssize_t col = 0; col < cols; ++col) {
            out(row, col) = values[static_cast<std::size_t>(row * cols + col)];
        }
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    std::initializer_list<double> values) {
    return make_matrix(rows, cols, std::vector<double>(values));
}

std::vector<double> make_periodic_prices(double scale) {
    std::vector<double> prices(41);
    prices[0] = scale;
    for (std::size_t i = 1; i < prices.size(); ++i) {
        const double factor = ((i - 1) % 2 == 0) ? 2.0 : 4.0;
        prices[i] = prices[i - 1] * factor;
    }
    return prices;
}

struct OhlcVectors {
    std::vec…27254 chars truncated…ore 原生 C++ 算法测试
+ *
+ * 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17
+ */
+
+#define DOCTEST_CONFIG_IMPLEMENT
+#include <doctest/doctest.h>
+
+#include <pybind11/embed.h>
+#include <pybind11/numpy.h>
+
+#include <array>
+#include <cmath>
+#include <cstdint>
+#include <limits>
+#include <stdexcept>
+#include <vector>
+
+namespace py = pybind11;
+
+using ArrD = py::array_t<double, py::array::c_style | py::array::forcecast>;
+using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;
+
+// etf_core.cpp 当前没有公共 C++ 头文件，因此在此声明原生入口。
+// 测试直接调用这些符号，不导入 Python 扩展模块，也不测试绑定分发层。
+ArrD standardize_returns(ArrD price_series);
+double cosine_similarity(ArrD x_arr, ArrD y_arr);
+double dtw_distance(ArrD x_arr, ArrD y_arr, int window);
+py::object dtw_distance_batch(ArrD query_arr, ArrD candidates_arr, int window, int top_k);
+double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
+ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
+py::object pattern_match_single(
+    ArrD prices_arr,
diff --git a/tests/CMakeLists.txt b/tests/CMakeLists.txt
new file mode 100644
index 0000000..2d95677
--- /dev/null
+++ b/tests/CMakeLists.txt
@@ -0,0 +1,95 @@
+cmake_minimum_required(VERSION 3.20)
+
+# etf_core 原生 C++ 测试
+# 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17
+
+if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
+    project(etf_core_native_tests LANGUAGES CXX)
+endif()
+
+set(CMAKE_CXX_STANDARD 20)
+set(CMAKE_CXX_STANDARD_REQUIRED ON)
+set(CMAKE_CXX_EXTENSIONS OFF)
+
+# 测试直接调用含 py::array_t 参数的 C++ 入口，因此需要嵌入式 Python 运行时。
+set(Python_EXECUTABLE "" CACHE FILEPATH "Path to python.exe")
+if(Python_EXECUTABLE)
+    get_filename_component(Python_ROOT_DIR "${Python_EXECUTABLE}" DIRECTORY)
+endif()
+find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Embed)
+
+# pybind11 — 与项目根 CMakeLists.txt 使用相同的自动探测策略。
+set(pybind11_DIR "" CACHE PATH "pybind11 cmake config dir")
+if(NOT pybind11_DIR)
+    execute_process(
+        COMMAND "${Python_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
+        OUTPUT_VARIABLE _pybind11_cmake_dir
+        OUTPUT_STRIP_TRAILING_WHITESPACE
+        ERROR_QUIET
+    )
+    if(_pybind11_cmake_dir)
+        set(pybind11_DIR "${_pybind11_cmake_dir}")
+    endif()
+endif()
+if(NOT pybind11_DIR)
+    message(FATAL_ERROR
+        "pybind11 not found. Install it for the selected Python or set pybind11_DIR.")
+endif()
+find_package(pybind11 REQUIRED CONFIG)
+
+include(FetchContent)
+set(DOCTEST_WITH_TESTS OFF CACHE BOOL "" FORCE)
+FetchContent_Declare(
+    doctest
+    GIT_REPOSITORY https://github.com/doctest/doctest.git
+    GIT_TAG v2.4.11
+    GIT_SHALLOW TRUE
+)
+FetchContent_MakeAvailable(doctest)
+
+get_filename_component(ETF_PROJECT_ROOT "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)
+set(ETF_CORE_SOURCE "${ETF_PROJECT_ROOT}/src/cpp/etf_core.cpp")
+
+# 生产 target etf_core 是 MODULE_LIBRARY；CMake 禁止可执行文件直接链接 MODULE_LIBRARY。
+# 独立配置 tests/ 时，使用同一生产源文件创建可链接的静态 etf_core；若未来从根工程
+# add_subdirectory(tests)，则保留生产模块并创建仅供原生测试链接的 etf_core_native_link。
+if(TARGET etf_core)
+    get_target_property(_etf_core_type etf_core TYPE)
+endif()
+
+if(TARGET etf_core AND NOT _etf_core_type STREQUAL "MODULE_LIBRARY")
+    set(ETF_CORE_NATIVE_TARGET etf_core)
+elseif(TARGET etf_core)
+    set(ETF_CORE_NATIVE_TARGET etf_core_native_link)
+    if(NOT TARGET ${ETF_CORE_NATIVE_TARGET})
+        add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
+        target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
+        target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
+    endif()
+else()
+    set(ETF_CORE_NATIVE_TARGET etf_core)
+    add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
+    target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
+    target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
+endif()
+
+add_executable(test_native test_etf_core.cpp)
+target_compile_features(test_native PRIVATE cxx_std_20)
+target_link_libraries(
+    test_native
+    PRIVATE
+        doctest::doctest
+        ${ETF_CORE_NATIVE_TARGET}
+        pybind11::embed
+)
+
+if(MSVC)
+    target_compile_options(test_native PRIVATE /utf-8 /wd4819)
+    if(ETF_CORE_NATIVE_TARGET STREQUAL "etf_core_native_link"
+       OR (ETF_CORE_NATIVE_TARGET STREQUAL "etf_core" AND NOT _etf_core_type))
+        target_compile_options(${ETF_CORE_NATIVE_TARGET} PRIVATE /utf-8 /wd4819)
+    endif()
+endif()
+
+enable_testing()
+add_test(NAME test_native COMMAND test_native)
\ No newline at end of file

 exited 1 in 264ms:
--- tests/test_etf_core.cpp ---
/**
 * test_etf_core.cpp — etf_core 原生 C++ 算法测试
 *
 * 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17
 */

#define DOCTEST_CONFIG_IMPLEMENT
#include <doctest/doctest.h>

#include <pybind11/embed.h>
#include <pybind11/numpy.h>

#include <array>
#include <cmath>
#include <cstdint>
#include <limits>
#include <stdexcept>
#include <vector>

namespace py = pybind11;

using ArrD = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;

// etf_core.cpp 当前没有公共 C++ 头文件，因此在此声明原生入口。
// 测试直接调用这些符号，不导入 Python 扩展模块，也不测试绑定分发层。
ArrD standardize_returns(ArrD price_series);
double cosine_similarity(ArrD x_arr, ArrD y_arr);
double dtw_distance(ArrD x_arr, ArrD y_arr, int window);
py::object dtw_distance_batch(ArrD query_arr, ArrD candidates_arr, int window, int top_k);
double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
py::object pattern_match_single(
    ArrD prices_arr,
    int T_idx,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);
py::tuple pattern_match_batch(
    ArrD prices_arr,
    ArrI64 t_indices_arr,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);

// 非有限值策略（由 etf_core.cpp 的当前实现定义）：
// 1. standardize_returns 对价格窗口执行有限性检查；任一 NaN/Inf 都拒绝整个窗口并返回空数组。
// 2. cosine_similarity 与 DTW 不预先拒绝 NaN/Inf，而是按 IEEE-754 传播；Inf/Inf 等不定式产生 NaN。
// 3. compute_adx 与 compute_atr 不预先拒绝 NaN/Inf；ADX 中 Inf/Inf 可变为 NaN，ATR 保留 NaN/Inf。
// 4. pattern_match_single/batch 通过标准化步骤拒绝含 NaN/Inf 的查询窗口；single 返回 None，batch 标记无效。

namespace {

constexpr int kPatternTIdx = 30;
constexpr int kPatternK = 50;
constexpr int kPatternQueryLength = 3;
constexpr int kPatternLookback = 100;
constexpr int kPatternStep = 1;
constexpr int kPatternForward = 1;
constexpr int kPatternDtwWindow = 1;
constexpr int kPatternPrefilterTop = 50;

constexpr std::array<const char*, 15> kFeatureKeys = {
    "top1_sim",
    "top5_avg_sim",
    "sim_decay",
    "sim_variance",
    "match_distance_ratio",
    "avg_future_ret",
    "weighted_future_ret",
    "median_future_ret",
    "ret_sign_consistency",
    "best_match_ret",
    "max_dd_in_matches",
    "match_time_span",
    "match_time_span_ratio",
    "match_cluster_ratio",
    "n_matches_above_thresh",
};

constexpr std::array<double, 15> kPeriodicExpectedFeatures = {
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    0.0,
    24.0,
    0.24,
    1.0,
    0.0,
};

ArrD make_array(const std::vector<double>& values) {
    ArrD result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_array(std::initializer_list<double> values) {
    return make_array(std::vector<double>(values));
}

ArrI64 make_index_array(const std::vector<int64_t>& values) {
    ArrI64 result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    const std::vector<double>& values) {
    if (values.size() != static_cast<std::size_t>(rows * cols)) {
        throw std::invalid_argument("matrix data size does not match shape");
    }

    ArrD result(std::vector<py::ssize_t>{rows, cols});
    auto out = result.mutable_unchecked<2>();
    for (py::ssize_t row = 0; row < rows; ++row) {
        for (py::ssize_t col = 0; col < cols; ++col) {
            out(row, col) = values[static_cast<std::size_t>(row * cols + col)];
        }
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    std::initializer_list<double> values) {
    return make_matrix(rows, cols, std::vector<double>(values));
}

std::vector<double> make_periodic_prices(double scale) {
    std::vector<double> prices(41);
    prices[0] = scale;
    for (std::size_t i = 1; i < prices.size(); ++i) {
        const double factor = ((i - 1) % 2 == 0) ? 2.0 : 4.0;
        prices[i] = prices[i - 1] * factor;
    }
    return prices;
}

struct OhlcVectors {
    std::vector<double> high;
    std::vector<double> low;
    std::vector<double> close;
};

OhlcVectors make_trending_ohlc(double scale) {
    OhlcVectors data;
    data.high.resize(18);
    data.low.resize(18);
    data.close.resize(18);

    for (std::size_t i = 0; i < data.close.size(); ++i) {
        data.close[i] = (static_cast<double>(i) + 2.0) * scale;
        data.high[i] = data.close[i] + 0.5 * scale;
        data.low[i] = data.close[i] - 0.5 * scale;
    }
    return data;
}

OhlcVectors make_known_atr_input(double scale = 1.0) {
    return {
        {10.0 * scale, 12.0 * scale, 13.0 * scale, 15.0 * scale},
        {8.0 * scale, 9.0 * scale, 11.0 * scale, 12.0 * scale},
        {9.0 * scale, 11.0 * scale, 12.0 * scale, 14.0 * scale},
    };
}

py::object run_pattern_single(const std::vector<double>& prices, int t_idx = kPatternTIdx) {
    return pattern_match_single(
        make_array(prices),
        t_idx,
        kPatternK,
        kPatternQueryLength,
        kPatternLookback,
        kPatternStep,
        kPatternForward,
        kPatternDtwWindow,
        kPatternPrefilterTop);
}

py::tuple run_pattern_batch(
    const std::vector<double>& prices,
    const std::vector<int64_t>& t_indices) {
    return pattern_match_batch(
        make_array(prices),
        make_index_array(t_indices),
        kPatternK,
        kPatternQueryLength,
        kPatternLookback,
        kPatternStep,
        kPatternForward,
        kPatternDtwWindow,
        kPatternPrefilterTop);
}

std::array<double, 15> values_from_dict(const py::dict& result) {
    std::array<double, 15> values{};
    for (std::size_t i = 0; i < kFeatureKeys.size(); ++i) {
        values[i] = py::cast<double>(result[py::str(kFeatureKeys[i])]);
    }
    return values;
}

std::array<double, 15> values_from_batch_row(const ArrD& features, py::ssize_t row) {
    const auto data = features.unchecked<2>();
    std::array<double, 15> values{};
    for (py::ssize_t col = 0; col < 15; ++col) {
        values[static_cast<std::size_t>(col)] = data(row, col);
    }
    return values;
}

void check_periodic_expected_features(const std::array<double, 15>& actual) {
    for (std::size_t i = 0; i < actual.size(); ++i) {
        CAPTURE(i);
        CHECK(actual[i] == doctest::Approx(kPeriodicExpectedFeatures[i]).epsilon(1e-12));
    }
}

} // namespace

int main(int argc, char** argv) {
    py::scoped_interpreter interpreter{};
    doctest::Context context(argc, argv);
    return context.run();
}

TEST_CASE("standardize_returns covers edge cases and a hand-computed result") {
    SUBCASE("empty input returns an empty array") {
        const ArrD result = standardize_returns(make_array({}));
        CHECK(result.ndim() == 1);
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("single price returns an empty array") {
        const ArrD result = standardize_returns(make_array({42.0}));
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("NaN and Inf reject the whole price window") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(standardize_returns(make_array({1.0, nan, 2.0})).shape(0) == 0);
        CHECK(standardize_returns(make_array({1.0, inf, 2.0})).shape(0) == 0);
    }

    SUBCASE("very small prices are floored and become zero returns") {
        const double tiny = std::ldexp(1.0, -900);
        const ArrD result = standardize_returns(make_array({tiny, 2.0 * tiny, 8.0 * tiny}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(0.0));
        CHECK(out(1) == doctest::Approx(0.0));
    }

    SUBCASE("very large finite prices remain numerically stable") {
        const double huge = std::ldexp(1.0, 900);
        const ArrD result = standardize_returns(make_array({huge, 2.0 * huge, 8.0 * huge}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(-1.0).epsilon(1e-12));
        CHECK(out(1) == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known answer for prices 1, 2, 8 is -1, 1") {
        const ArrD result = standardize_returns(make_array({1.0, 2.0, 8.0}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(-1.0).epsilon(1e-12));
        CHECK(out(1) == doctest::Approx(1.0).epsilon(1e-12));
    }
}

TEST_CASE("cosine_similarity covers edge cases and a hand-computed result") {
    SUBCASE("empty vectors return the neutral similarity zero") {
        CHECK(cosine_similarity(make_array({}), make_array({})) == doctest::Approx(0.0));
    }

    SUBCASE("single positive elements have similarity one") {
        CHECK(cosine_similarity(make_array({2.0}), make_array({3.0})) == doctest::Approx(1.0));
    }

    SUBCASE("NaN and Inf propagate to NaN") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(std::isnan(cosine_similarity(make_array({nan}), make_array({1.0}))));
        CHECK(std::isnan(cosine_similarity(make_array({inf}), make_array({1.0}))));
    }

    SUBCASE("very small norm returns zero and huge squaring overflow returns NaN") {
        CHECK(cosine_similarity(make_array({1e-300}), make_array({1.0})) == doctest::Approx(0.0));
        CHECK(std::isnan(cosine_similarity(make_array({1e308}), make_array({1e308}))));
    }

    SUBCASE("known answer is four fifths") {
        CHECK(cosine_similarity(make_array({1.0, 2.0}), make_array({2.0, 1.0}))
              == doctest::Approx(0.8).epsilon(1e-12));
    }

    SUBCASE("mismatched lengths are rejected") {
        CHECK_THROWS_AS(
            cosine_similarity(make_array({1.0}), make_array({1.0, 2.0})),
            std::invalid_argument);
    }
}

TEST_CASE("dtw_distance covers ties, window boundaries, and numeric policies") {
    SUBCASE("an empty sequence returns infinity") {
        CHECK(std::isinf(dtw_distance(make_array({}), make_array({1.0}), 1)));
        CHECK(std::isinf(dtw_distance(make_array({1.0}), make_array({}), 1)));
    }

    SUBCASE("single elements use sqrt squared cost divided by total length") {
        CHECK(dtw_distance(make_array({2.0}), make_array({5.0}), 0)
              == doctest::Approx(1.5).epsilon(1e-12));
    }

    SUBCASE("NaN propagates and finite versus Inf returns Inf") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(std::isnan(dtw_distance(make_array({nan}), make_array({0.0}), 0)));
        CHECK(std::isinf(dtw_distance(make_array({inf}), make_array({0.0}), 0)));
    }

    SUBCASE("very large and very small finite costs remain representable") {
        CHECK(dtw_distance(make_array({1e150}), make_array({-1e150}), 0)
              == doctest::Approx(1e150).epsilon(1e-12));
        CHECK(dtw_distance(make_array({1e-150}), make_array({-1e-150}), 0) / 1e-150
              == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known diagonal answer is one quarter") {
        CHECK(dtw_distance(make_array({0.0, 1.0}), make_array({0.0, 2.0}), 0)
              == doctest::Approx(0.25).epsilon(1e-12));
    }

    SUBCASE("equal predecessor ties stay deterministic in distance") {
        CHECK(dtw_distance(make_array({0.0, 0.0}), make_array({0.0, 0.0, 0.0}), 0)
              == doctest::Approx(0.0));
    }

    SUBCASE("window zero enforces the diagonal and window one permits warping") {
        const ArrD x = make_array({0.0, 1.0, 1.0});
        const ArrD y = make_array({0.0, 0.0, 1.0});
        CHECK(dtw_distance(x, y, 0) == doctest::Approx(1.0 / 6.0).epsilon(1e-12));
        CHECK(dtw_distance(x, y, 1) == doctest::Approx(0.0));
    }
}

TEST_CASE("dtw_distance_batch matches scalar DTW and honors Top-K ties") {
    SUBCASE("empty candidates return empty arrays in both modes") {
        const py::object all_result = dtw_distance_batch(
            make_array({}), make_matrix(0, 0, {}), 0, 0);
        const ArrD all_distances = py::reinterpret_borrow<ArrD>(all_result);
        CHECK(all_distances.shape(0) == 0);

        const py::object top_result = dtw_distance_batch(
            make_array({}), make_matrix(0, 0, {}), 0, 1);
        REQUIRE(py::isinstance<py::tuple>(top_result));
        const py::tuple top = py::reinterpret_borrow<py::tuple>(top_result);
        const ArrI64 indices = top[0].cast<ArrI64>();
        const ArrD distances = top[1].cast<ArrD>();
        CHECK(indices.shape(0) == 0);
        CHECK(distances.shape(0) == 0);
    }

    SUBCASE("one query value and one candidate produce the scalar answer") {
        const py::object result = dtw_distance_batch(
            make_array({2.0}), make_matrix(1, 1, {5.0}), 0, 0);
        const ArrD distances = py::reinterpret_borrow<ArrD>(result);
        const auto out = distances.unchecked<1>();
        REQUIRE(out.shape(0) == 1);
        CHECK(out(0) == doctest::Approx(1.5).epsilon(1e-12));
    }

    SUBCASE("NaN and Inf propagate per candidate row") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        const py::object result = dtw_distance_batch(
            make_array({0.0}), make_matrix(2, 1, {nan, inf}), 0, 0);
        const auto out = py::reinterpret_borrow<ArrD>(result).unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(std::isnan(out(0)));
        CHECK(std::isinf(out(1)));
    }

    SUBCASE("very large and very small candidates match scalar policy") {
        const py::object large_result = dtw_distance_batch(
            make_array({1e150}), make_matrix(1, 1, {-1e150}), 0, 0);
        const auto large = py::reinterpret_borrow<ArrD>(large_result).unchecked<1>();
        CHECK(large(0) == doctest::Approx(1e150).epsilon(1e-12));

        const py::object small_result = dtw_distance_batch(
            make_array({1e-150}), make_matrix(1, 1, {-1e-150}), 0, 0);
        const auto small = py::reinterpret_borrow<ArrD>(small_result).unchecked<1>();
        CHECK(small(0) / 1e-150 == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known candidate distances are zero and one quarter") {
        const py::object result = dtw_distance_batch(
            make_array({0.0, 1.0}),
            make_matrix(2, 2, {0.0, 1.0, 0.0, 2.0}),
            0,
            0);
        const auto out = py::reinterpret_borrow<ArrD>(result).unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(0.0));
        CHECK(out(1) == doctest::Approx(0.25).epsilon(1e-12));
    }

    SUBCASE("Top-K breaks equal-distance ties by candidate index") {
        const py::object result = dtw_distance_batch(
            make_array({0.0, 1.0}),
            make_matrix(3, 2, {0.0, 1.0, 0.0, 1.0, 1.0, 1.0}),
            0,
            2);
        REQUIRE(py::isinstance<py::tuple>(result));
        const py::tuple top = py::reinterpret_borrow<py::tuple>(result);
        const auto indices = top[0].cast<ArrI64>().unchecked<1>();
        const auto distances = top[1].cast<ArrD>().unchecked<1>();
        REQUIRE(indices.shape(0) == 2);
        CHECK(indices(0) == 0);
        CHECK(indices(1) == 1);
        CHECK(distances(0) == doctest::Approx(0.0));
        CHECK(distances(1) == doctest::Approx(0.0));
    }

    SUBCASE("batch mode observes the same boundary window behavior") {
        const ArrD query = make_array({0.0, 1.0, 1.0});
        const ArrD candidates = make_matrix(1, 3, {0.0, 0.0, 1.0});
        const py::object diagonal_result = dtw_distance_batch(query, candidates, 0, 0);
        const py::object warped_result = dtw_distance_batch(query, candidates, 1, 0);
        const auto diagonal = py::reinterpret_borrow<ArrD>(diagonal_result).unchecked<1>();
        const auto warped = py::reinterpret_borrow<ArrD>(warped_result).unchecked<1>();
        CHECK(diagonal(0) == doctest::Approx(1.0 / 6.0).epsilon(1e-12));
        CHECK(warped(0) == doctest::Approx(0.0));
    }
}

TEST_CASE("compute_adx covers neutral, propagation, extremes, and known answers") {
    SUBCASE("empty input returns the neutral ADX value") {
        CHECK(compute_adx(make_array({}), make_array({}), make_array({}), 14)
              == doctest::Approx(25.0));
    }

    SUBCASE("a single OHLC point also returns the neutral ADX value") {
        CHECK(compute_adx(make_array({10.0}), make_array({9.0}), make_array({9.5}), 14)
              == doctest::Approx(25.0));
    }

    SUBCASE("NaN and Inf propagate to NaN for a full calculation window") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        OhlcVectors nan_data = make_trending_ohlc(1.0);
        nan_data.high[1] = nan;
        CHECK(std::isnan(compute_adx(
            make_array(nan_data.high), make_array(nan_data.low), make_array(nan_data.close), 2)));

        OhlcVectors inf_data = make_trending_ohlc(1.0);
        inf_data.high[1] = inf;
        CHECK(std::isnan(compute_adx(
            make_array(inf_data.high), make_array(inf_data.low), make_array(inf_data.close), 2)));
    }

    SUBCASE("very large trend approaches one hundred without overflow") {
        const OhlcVectors data = make_trending_ohlc(std::ldexp(1.0, 900));
        const double result = compute_adx(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        CHECK(std::isfinite(result));
        CHECK(result == doctest::Approx(100.0).epsilon(1e-12));
    }

    SUBCASE("very small trend is dominated by the fixed epsilon but remains finite") {
        const OhlcVectors data = make_trending_ohlc(std::ldexp(1.0, -900));
        const double result = compute_adx(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        CHECK(std::isfinite(result));
        CHECK(result >= 0.0);
        CHECK(result < 1e-200);
    }

    SUBCASE("flat prices have known ADX zero") {
        const std::vector<double> flat(18, 10.0);
        CHECK(compute_adx(make_array(flat), make_array(flat), make_array(flat), 2)
              == doctest::Approx(0.0));
    }
}

TEST_CASE("compute_atr covers short inputs, propagation, scaling, and a known series") {
    SUBCASE("empty input returns an empty array") {
        const ArrD result = compute_atr(make_array({}), make_array({}), make_array({}), 14);
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("a single point returns one NaN because the warmup is incomplete") {
        const ArrD result = compute_atr(
            make_array({10.0}), make_array({9.0}), make_array({9.5}), 14);
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 1);
        CHECK(std::isnan(out(0)));
    }

    SUBCASE("NaN propagates and Inf is preserved by Wilder smoothing") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        OhlcVectors nan_data = make_known_atr_input();
        nan_data.high[2] = nan;
        const auto nan_out = compute_atr(
            make_array(nan_data.high), make_array(nan_data.low), make_array(nan_data.close), 2)
                                 .unchecked<1>();
        CHECK(std::isnan(nan_out(2)));
        CHECK(std::isnan(nan_out(3)));

        OhlcVectors inf_data = make_known_atr_input();
        inf_data.high[2] = inf;
        const auto inf_out = compute_atr(
            make_array(inf_data.high), make_array(inf_data.low), make_array(inf_data.close), 2)
                                 .unchecked<1>();
        CHECK(std::isinf(inf_out(2)));
        CHECK(std::isinf(inf_out(3)));
    }

    SUBCASE("very large and very small finite inputs scale linearly") {
        for (const double scale : {std::ldexp(1.0, 900), std::ldexp(1.0, -900)}) {
            CAPTURE(scale);
            const OhlcVectors data = make_known_atr_input(scale);
            const auto out = compute_atr(
                make_array(data.high), make_array(data.low), make_array(data.close), 2)
                                 .unchecked<1>();
            CHECK(out(2) / scale == doctest::Approx(2.5).epsilon(1e-12));
            CHECK(out(3) / scale == doctest::Approx(2.75).epsilon(1e-12));
        }
    }

    SUBCASE("known ATR is NaN, NaN, 2.5, 2.75") {
        const OhlcVectors data = make_known_atr_input();
        const ArrD result = compute_atr(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 4);
        CHECK(std::isnan(out(0)));
        CHECK(std::isnan(out(1)));
        CHECK(out(2) == doctest::Approx(2.5).epsilon(1e-12));
        CHECK(out(3) == doctest::Approx(2.75).epsilon(1e-12));
    }
}

TEST_CASE("pattern_match_single covers invalid indices and deterministic features") {
    SUBCASE("empty prices reject T_idx as out of range without a native crash") {
        CHECK_THROWS_AS(run_pattern_single({}, 0), std::out_of_range);
    }

    SUBCASE("one price is valid input but has insufficient history and returns None") {
        const py::object result = run_pattern_single({1.0}, 0);
        CHECK(result.is_none());
    }

    SUBCASE("negative and one-past-end T_idx are rejected") {
        const std::vector<double> prices = {1.0, 2.0, 4.0};
        CHECK_THROWS_AS(run_pattern_single(prices, -1), std::out_of_range);
        CHECK_THROWS_AS(run_pattern_single(prices, 3), std::out_of_range);
    }

    SUBCASE("NaN and Inf in the query window are rejected as None") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        std::vector<double> nan_prices = make_periodic_prices(1.0);
        nan_prices[kPatternTIdx] = nan;
        CHECK(run_pattern_single(nan_prices).is_none());

        std::vector<double> inf_prices = make_periodic_prices(1.0);
        inf_prices[kPatternTIdx] = inf;
        CHECK(run_pattern_single(inf_prices).is_none());
    }

    SUBCASE("very large powers of two preserve the deterministic known features") {
        const py::object result = run_pattern_single(
            make_periodic_prices(std::ldexp(1.0, 900)));
        REQUIRE_FALSE(result.is_none());
        REQUIRE(py::isinstance<py::dict>(result));
        check_periodic_expected_features(
            values_from_dict(py::reinterpret_borrow<py::dict>(result)));
    }

    SUBCASE("very small prices are floored, lose shape, and return None") {
        const py::object result = run_pattern_single(
            make_periodic_prices(std::ldexp(1.0, -900)));
        CHECK(result.is_none());
    }

    SUBCASE("periodic prices have a hand-derived 15-feature answer") {
        const py::object result = run_pattern_single(make_periodic_prices(1.0));
        REQUIRE_FALSE(result.is_none());
        REQUIRE(py::isinstance<py::dict>(result));
        check_periodic_expected_features(
            values_from_dict(py::reinterpret_borrow<py::dict>(result)));
    }
}

TEST_CASE("pattern_match_batch covers masks, extremes, and deterministic features") {
    SUBCASE("empty prices and indices return shapes zero by fifteen and zero") {
        const py::tuple result = run_pattern_batch({}, {});
        const ArrD features = result[0].cast<ArrD>();
        const py::array_t<bool> mask = result[1].cast<py::array_t<bool>>();
        CHECK(features.ndim() == 2);
        CHECK(features.shape(0) == 0);
        CHECK(features.shape(1) == 15);
        CHECK(mask.shape(0) == 0);
    }

    SUBCASE("one price yields no feature row and a false validity mask") {
        const py::tuple result = run_pattern_batch({1.0}, {0});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        CHECK(features.shape(0) == 0);
        REQUIRE(mask.shape(0) == 1);
        CHECK_FALSE(mask(0));
    }

    SUBCASE("NaN and Inf in the query window produce false masks") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        for (const double bad_value : {nan, inf}) {
            std::vector<double> prices = make_periodic_prices(1.0);
            prices[kPatternTIdx] = bad_value;
            const py::tuple result = run_pattern_batch(prices, {kPatternTIdx});
            const ArrD features = result[0].cast<ArrD>();
            const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
            CHECK(features.shape(0) == 0);
            REQUIRE(mask.shape(0) == 1);
            CHECK_FALSE(mask(0));
        }
    }

    SUBCASE("very large powers of two preserve one known feature row") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(std::ldexp(1.0, 900)), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        REQUIRE(features.shape(0) == 1);
        REQUIRE(features.shape(1) == 15);
        REQUIRE(mask.shape(0) == 1);
        CHECK(mask(0));
        check_periodic_expected_features(values_from_batch_row(features, 0));
    }

    SUBCASE("very small prices produce no feature rows and a false mask") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(std::ldexp(1.0, -900)), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        CHECK(features.shape(0) == 0);
        REQUIRE(mask.shape(0) == 1);
        CHECK_FALSE(mask(0));
    }

    SUBCASE("periodic prices have the same hand-derived feature row as single mode") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(1.0), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        REQUIRE(features.shape(0) == 1);
        REQUIRE(features.shape(1) == 15);
        REQUIRE(mask.shape(0) == 1);
        CHECK(mask(0));
        check_periodic_expected_features(values_from_batch_row(features, 0));
    }
}
--- tests/CMakeLists.txt ---
cmake_minimum_required(VERSION 3.20)

# etf_core 原生 C++ 测试
# 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17

if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    project(etf_core_native_tests LANGUAGES CXX)
endif()

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# 测试直接调用含 py::array_t 参数的 C++ 入口，因此需要嵌入式 Python 运行时。
set(Python_EXECUTABLE "" CACHE FILEPATH "Path to python.exe")
if(Python_EXECUTABLE)
    get_filename_component(Python_ROOT_DIR "${Python_EXECUTABLE}" DIRECTORY)
endif()
find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Embed)

# pybind11 — 与项目根 CMakeLists.txt 使用相同的自动探测策略。
set(pybind11_DIR "" CACHE PATH "pybind11 cmake config dir")
if(NOT pybind11_DIR)
    execute_process(
        COMMAND "${Python_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE _pybind11_cmake_dir
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )
    if(_pybind11_cmake_dir)
        set(pybind11_DIR "${_pybind11_cmake_dir}")
    endif()
endif()
if(NOT pybind11_DIR)
    message(FATAL_ERROR
        "pybind11 not found. Install it for the selected Python or set pybind11_DIR.")
endif()
find_package(pybind11 REQUIRED CONFIG)

include(FetchContent)
set(DOCTEST_WITH_TESTS OFF CACHE BOOL "" FORCE)
FetchContent_Declare(
    doctest
    GIT_REPOSITORY https://github.com/doctest/doctest.git
    GIT_TAG v2.4.11
    GIT_SHALLOW TRUE
)
FetchContent_MakeAvailable(doctest)

get_filename_component(ETF_PROJECT_ROOT "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)
set(ETF_CORE_SOURCE "${ETF_PROJECT_ROOT}/src/cpp/etf_core.cpp")

# 生产 target etf_core 是 MODULE_LIBRARY；CMake 禁止可执行文件直接链接 MODULE_LIBRARY。
# 独立配置 tests/ 时，使用同一生产源文件创建可链接的静态 etf_core；若未来从根工程
# add_subdirectory(tests)，则保留生产模块并创建仅供原生测试链接的 etf_core_native_link。
if(TARGET etf_core)
    get_target_property(_etf_core_type etf_core TYPE)
endif()

if(TARGET etf_core AND NOT _etf_core_type STREQUAL "MODULE_LIBRARY")
    set(ETF_CORE_NATIVE_TARGET etf_core)
elseif(TARGET etf_core)
    set(ETF_CORE_NATIVE_TARGET etf_core_native_link)
    if(NOT TARGET ${ETF_CORE_NATIVE_TARGET})
        add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
        target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
        target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
    endif()
else()
    set(ETF_CORE_NATIVE_TARGET etf_core)
    add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
    target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
    target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
endif()

add_executable(test_native test_etf_core.cpp)
target_compile_features(test_native PRIVATE cxx_std_20)
target_link_libraries(
    test_native
    PRIVATE
        doctest::doctest
        ${ETF_CORE_NATIVE_TARGET}
        pybind11::embed
)

if(MSVC)
    target_compile_options(test_native PRIVATE /utf-8 /wd4819)
    if(ETF_CORE_NATIVE_TARGET STREQUAL "etf_core_native_link"
       OR (ETF_CORE_NATIVE_TARGET STREQUAL "etf_core" AND NOT _etf_core_type))
        target_compile_options(${ETF_CORE_NATIVE_TARGET} PRIVATE /utf-8 /wd4819)
    endif()
endif()

enable_testing()
add_test(NAME test_native COMMAND test_native)
--- encoding and line endings ---
tests/test_etf_core.cpp: bytes=27909, UTF8_BOM=False, CRLF=695, bare_LF=0
tests/CMakeLists.txt: bytes=3610, UTF8_BOM=False, CRLF=94, bare_LF=0
--- git diff --stat/status ---
 M project_status.md
?? _review/
?? docs/reviews/performance-analysis-review-kimi.md
?? improvement_plan.md
?? notebooks/01_price_series.png
?? notebooks/02_query_window.png
?? notebooks/03_cosine_prefilter.png
?? notebooks/04_dtw_warping.png
?? notebooks/05_feature_evolution.png
?? notebooks/06_trading_signals.png
?? notebooks/07_batch_dtw.png
?? notebooks/08_benchmark.png
?? prompt_p0_build.md
?? prompt_p1_benchmark.md
?? tests/CMakeLists.txt
?? tests/test_etf_core.cpp
diff --git a/tests/test_etf_core.cpp b/tests/test_etf_core.cpp
new file mode 100644
index 0000000..7c2e81c
--- /dev/null
+++ b/tests/test_etf_core.cpp
@@ -0,0 +1,696 @@
+/**
+ * test_etf_core.cpp — etf_core 原生 C++ 算法测试
+ *
+ * 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17
+ */
+
+#define DOCTEST_CONFIG_IMPLEMENT
+#include <doctest/doctest.h>
+
+#include <pybind11/embed.h>
+#include <pybind11/numpy.h>
+
+#include <array>
+#include <cmath>
+#include <cstdint>
+#include <limits>
+#include <stdexcept>
+#include <vector>
+
+namespace py = pybind11;
+
+using ArrD = py::array_t<double, py::array::c_style | py::array::forcecast>;
+using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;
+
+// etf_core.cpp 当前没有公共 C++ 头文件，因此在此声明原生入口。
+// 测试直接调用这些符号，不导入 Python 扩展模块，也不测试绑定分发层。
+ArrD standardize_returns(ArrD price_series);
+double cosine_similarity(ArrD x_arr, ArrD y_arr);
+double dtw_distance(ArrD x_arr, ArrD y_arr, int window);
+py::object dtw_distance_batch(ArrD query_arr, ArrD candidates_arr, int window, int top_k);
+double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
+ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
+py::object pattern_match_single(
+    ArrD prices_arr,
diff --git a/tests/CMakeLists.txt b/tests/CMakeLists.txt
new file mode 100644
index 0000000..2d95677
--- /dev/null
+++ b/tests/CMakeLists.txt
@@ -0,0 +1,95 @@
+cmake_minimum_required(VERSION 3.20)
+
+# etf_core 原生 C++ 测试
+# 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17
+
+if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
+    project(etf_core_native_tests LANGUAGES CXX)
+endif()
+
+set(CMAKE_CXX_STANDARD 20)
+set(CMAKE_CXX_STANDARD_REQUIRED ON)
+set(CMAKE_CXX_EXTENSIONS OFF)
+
+# 测试直接调用含 py::array_t 参数的 C++ 入口，因此需要嵌入式 Python 运行时。
+set(Python_EXECUTABLE "" CACHE FILEPATH "Path to python.exe")
+if(Python_EXECUTABLE)
+    get_filename_component(Python_ROOT_DIR "${Python_EXECUTABLE}" DIRECTORY)
+endif()
+find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Embed)
+
+# pybind11 — 与项目根 CMakeLists.txt 使用相同的自动探测策略。
+set(pybind11_DIR "" CACHE PATH "pybind11 cmake config dir")
+if(NOT pybind11_DIR)
+    execute_process(
+        COMMAND "${Python_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
+        OUTPUT_VARIABLE _pybind11_cmake_dir
+        OUTPUT_STRIP_TRAILING_WHITESPACE
+        ERROR_QUIET
+    )
+    if(_pybind11_cmake_dir)
+        set(pybind11_DIR "${_pybind11_cmake_dir}")
+    endif()
+endif()
+if(NOT pybind11_DIR)
+    message(FATAL_ERROR
+        "pybind11 not found. Install it for the selected Python or set pybind11_DIR.")
+endif()
+find_package(pybind11 REQUIRED CONFIG)
+
+include(FetchContent)
+set(DOCTEST_WITH_TESTS OFF CACHE BOOL "" FORCE)
+FetchContent_Declare(
+    doctest
+    GIT_REPOSITORY https://github.com/doctest/doctest.git
+    GIT_TAG v2.4.11
+    GIT_SHALLOW TRUE
+)
+FetchContent_MakeAvailable(doctest)
+
+get_filename_component(ETF_PROJECT_ROOT "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)
+set(ETF_CORE_SOURCE "${ETF_PROJECT_ROOT}/src/cpp/etf_core.cpp")
+
+# 生产 target etf_core 是 MODULE_LIBRARY；CMake 禁止可执行文件直接链接 MODULE_LIBRARY。
+# 独立配置 tests/ 时，使用同一生产源文件创建可链接的静态 etf_core；若未来从根工程
+# add_subdirectory(tests)，则保留生产模块并创建仅供原生测试链接的 etf_core_native_link。
+if(TARGET etf_core)
+    get_target_property(_etf_core_type etf_core TYPE)
+endif()
+
+if(TARGET etf_core AND NOT _etf_core_type STREQUAL "MODULE_LIBRARY")
+    set(ETF_CORE_NATIVE_TARGET etf_core)
+elseif(TARGET etf_core)
+    set(ETF_CORE_NATIVE_TARGET etf_core_native_link)
+    if(NOT TARGET ${ETF_CORE_NATIVE_TARGET})
+        add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
+        target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
+        target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
+    endif()
+else()
+    set(ETF_CORE_NATIVE_TARGET etf_core)
+    add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
+    target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
+    target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
+endif()
+
+add_executable(test_native test_etf_core.cpp)
+target_compile_features(test_native PRIVATE cxx_std_20)
+target_link_libraries(
+    test_native
+    PRIVATE
+        doctest::doctest
+        ${ETF_CORE_NATIVE_TARGET}
+        pybind11::embed
+)
+
+if(MSVC)
+    target_compile_options(test_native PRIVATE /utf-8 /wd4819)
+    if(ETF_CORE_NATIVE_TARGET STREQUAL "etf_core_native_link"
+       OR (ETF_CORE_NATIVE_TARGET STREQUAL "etf_core" AND NOT _etf_core_type))
+        target_compile_options(${ETF_CORE_NATIVE_TARGET} PRIVATE /utf-8 /wd4819)
+    endif()
+endif()
+
+enable_testing()
+add_test(NAME test_native COMMAND test_native)
\ No newline at end of file

warning: Skill descriptions were shortened to fit the 2% skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
context compacted
warning: Heads up: Long threads and multiple compactions can cause the model to be less accurate. Start a new thread when possible to keep threads small and targeted.
