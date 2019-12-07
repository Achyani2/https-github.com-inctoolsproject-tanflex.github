<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>git_find_releases.py - chromium/tools/depot_tools.git - Git at Google</title><link rel="stylesheet" type="text/css" href="/+static/base.vsKBklzePi_Td7VvkjGVKw.cache.css"><link rel="stylesheet" type="text/css" href="/+static/prettify/prettify.pZ5FqzM6cPxAflH0va2Ucw.cache.css"><!-- default customHeadTagPart --></head><body class="Site"><header class="Site-header"><div class="Header"><a class="Header-image" href="/"><img src="//www.gstatic.com/images/branding/lockups/2x/lockup_git_color_108x24dp.png" width="108" height="24" alt="Google Git"></a><div class="Header-menu"> <a class="Header-menuItem" href="https://accounts.google.com/AccountChooser?service=gerritcodereview&amp;continue=https://chromium.googlesource.com/login/chromium/tools/depot_tools.git/%2B/refs/heads/master/git_find_releases.py">Switch user</a> <a class="Header-menuItem" href="https://chromium.googlesource.com/+logout?continue=/chromium/tools/depot_tools.git/%2B/refs/heads/master/git_find_releases.py">Sign out</a> <span class="Header-menuItem Header-menuItem--noAction">‪pratan niamjoi‬ &lt;tanknug1983@gmail.com&gt;</span> </div></div></header><div class="Site-content"><div class="Container "><div class="Breadcrumbs"><a class="Breadcrumbs-crumb" href="/?format=HTML">chromium</a> / <a class="Breadcrumbs-crumb" href="/chromium/">chromium</a> / <a class="Breadcrumbs-crumb" href="/chromium/tools/">tools</a> / <a class="Breadcrumbs-crumb" href="/chromium/tools/depot_tools.git/">depot_tools.git</a> / <a class="Breadcrumbs-crumb" href="/chromium/tools/depot_tools.git/+/refs/heads/master">refs/heads/master</a> / <a class="Breadcrumbs-crumb" href="/chromium/tools/depot_tools.git/+/refs/heads/master/">.</a> / <span class="Breadcrumbs-crumb">git_find_releases.py</span></div><div class="u-sha1 u-monospace BlobSha1">blob: cab723dd35b0ab83e198abc6c47d4f348925df02 [<a href="/chromium/tools/depot_tools.git/+/refs/heads/master/git_find_releases.py">file</a>] [<a href="/chromium/tools/depot_tools.git/+log/refs/heads/master/git_find_releases.py">log</a>] [<a href="/chromium/tools/depot_tools.git/+blame/refs/heads/master/git_find_releases.py">blame</a>]</div><table class="FileContents"><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="1" onclick="window.location.hash='#1'"></td><td class="FileContents-lineContents" id="1"><span class="com">#!/usr/bin/env python</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="2" onclick="window.location.hash='#2'"></td><td class="FileContents-lineContents" id="2"><span class="com"># Copyright 2015 The Chromium Authors. All rights reserved.</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="3" onclick="window.location.hash='#3'"></td><td class="FileContents-lineContents" id="3"><span class="com"># Use of this source code is governed by a BSD-style license that can be</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="4" onclick="window.location.hash='#4'"></td><td class="FileContents-lineContents" id="4"><span class="com"># found in the LICENSE file.</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="5" onclick="window.location.hash='#5'"></td><td class="FileContents-lineContents" id="5"><span class="str">&quot;&quot;&quot;Usage: %prog &lt;commit&gt;*</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="6" onclick="window.location.hash='#6'"></td><td class="FileContents-lineContents" id="6"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="7" onclick="window.location.hash='#7'"></td><td class="FileContents-lineContents" id="7"><span class="str">Given a commit, finds the release where it first appeared (e.g. 47.0.2500.0) as</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="8" onclick="window.location.hash='#8'"></td><td class="FileContents-lineContents" id="8"><span class="str">well as attempting to determine the branches to which it was merged.</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="9" onclick="window.location.hash='#9'"></td><td class="FileContents-lineContents" id="9"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="10" onclick="window.location.hash='#10'"></td><td class="FileContents-lineContents" id="10"><span class="str">Note that it uses the &quot;cherry picked from&quot; annotation to find merges, so it will</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="11" onclick="window.location.hash='#11'"></td><td class="FileContents-lineContents" id="11"><span class="str">only work on merges that followed the &quot;use cherry-pick -x&quot; instructions.</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="12" onclick="window.location.hash='#12'"></td><td class="FileContents-lineContents" id="12"><span class="str">&quot;&quot;&quot;</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="13" onclick="window.location.hash='#13'"></td><td class="FileContents-lineContents" id="13"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="14" onclick="window.location.hash='#14'"></td><td class="FileContents-lineContents" id="14"><span class="kwd">from</span><span class="pln"> __future__ </span><span class="kwd">import</span><span class="pln"> print_function</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="15" onclick="window.location.hash='#15'"></td><td class="FileContents-lineContents" id="15"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="16" onclick="window.location.hash='#16'"></td><td class="FileContents-lineContents" id="16"><span class="kwd">import</span><span class="pln"> optparse</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="17" onclick="window.location.hash='#17'"></td><td class="FileContents-lineContents" id="17"><span class="kwd">import</span><span class="pln"> re</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="18" onclick="window.location.hash='#18'"></td><td class="FileContents-lineContents" id="18"><span class="kwd">import</span><span class="pln"> sys</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="19" onclick="window.location.hash='#19'"></td><td class="FileContents-lineContents" id="19"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="20" onclick="window.location.hash='#20'"></td><td class="FileContents-lineContents" id="20"><span class="kwd">import</span><span class="pln"> git_common </span><span class="kwd">as</span><span class="pln"> git</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="21" onclick="window.location.hash='#21'"></td><td class="FileContents-lineContents" id="21"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="22" onclick="window.location.hash='#22'"></td><td class="FileContents-lineContents" id="22"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="23" onclick="window.location.hash='#23'"></td><td class="FileContents-lineContents" id="23"><span class="kwd">def</span><span class="pln"> </span><span class="typ">GetNameForCommit</span><span class="pun">(</span><span class="pln">sha1</span><span class="pun">):</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="24" onclick="window.location.hash='#24'"></td><td class="FileContents-lineContents" id="24"><span class="pln">  name </span><span class="pun">=</span><span class="pln"> re</span><span class="pun">.</span><span class="pln">sub</span><span class="pun">(</span><span class="pln">r</span><span class="str">&#39;~.*$&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;&#39;</span><span class="pun">,</span><span class="pln"> git</span><span class="pun">.</span><span class="pln">run</span><span class="pun">(</span><span class="str">&#39;name-rev&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--tags&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--name-only&#39;</span><span class="pun">,</span><span class="pln"> sha1</span><span class="pun">))</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="25" onclick="window.location.hash='#25'"></td><td class="FileContents-lineContents" id="25"><span class="pln">  </span><span class="kwd">if</span><span class="pln"> name </span><span class="pun">==</span><span class="pln"> </span><span class="str">&#39;undefined&#39;</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="26" onclick="window.location.hash='#26'"></td><td class="FileContents-lineContents" id="26"><span class="pln">    name </span><span class="pun">=</span><span class="pln"> git</span><span class="pun">.</span><span class="pln">run</span><span class="pun">(</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="27" onclick="window.location.hash='#27'"></td><td class="FileContents-lineContents" id="27"><span class="pln">        </span><span class="str">&#39;name-rev&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--refs&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;remotes/branch-heads/*&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--name-only&#39;</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="28" onclick="window.location.hash='#28'"></td><td class="FileContents-lineContents" id="28"><span class="pln">        sha1</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">&#39; [untagged]&#39;</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="29" onclick="window.location.hash='#29'"></td><td class="FileContents-lineContents" id="29"><span class="pln">  </span><span class="kwd">return</span><span class="pln"> name</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="30" onclick="window.location.hash='#30'"></td><td class="FileContents-lineContents" id="30"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="31" onclick="window.location.hash='#31'"></td><td class="FileContents-lineContents" id="31"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="32" onclick="window.location.hash='#32'"></td><td class="FileContents-lineContents" id="32"><span class="kwd">def</span><span class="pln"> </span><span class="typ">GetMergesForCommit</span><span class="pun">(</span><span class="pln">sha1</span><span class="pun">):</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="33" onclick="window.location.hash='#33'"></td><td class="FileContents-lineContents" id="33"><span class="pln">  </span><span class="kwd">return</span><span class="pln"> </span><span class="pun">[</span><span class="pln">c</span><span class="pun">.</span><span class="pln">split</span><span class="pun">()[</span><span class="lit">0</span><span class="pun">]</span><span class="pln"> </span><span class="kwd">for</span><span class="pln"> c </span><span class="kwd">in</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="34" onclick="window.location.hash='#34'"></td><td class="FileContents-lineContents" id="34"><span class="pln">          git</span><span class="pun">.</span><span class="pln">run</span><span class="pun">(</span><span class="str">&#39;log&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--oneline&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;-F&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--all&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--no-abbrev&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--grep&#39;</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="35" onclick="window.location.hash='#35'"></td><td class="FileContents-lineContents" id="35"><span class="pln">                  </span><span class="str">&#39;cherry picked from commit %s&#39;</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> sha1</span><span class="pun">).</span><span class="pln">splitlines</span><span class="pun">()]</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="36" onclick="window.location.hash='#36'"></td><td class="FileContents-lineContents" id="36"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="37" onclick="window.location.hash='#37'"></td><td class="FileContents-lineContents" id="37"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="38" onclick="window.location.hash='#38'"></td><td class="FileContents-lineContents" id="38"><span class="kwd">def</span><span class="pln"> main</span><span class="pun">():</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="39" onclick="window.location.hash='#39'"></td><td class="FileContents-lineContents" id="39"><span class="pln">  parser </span><span class="pun">=</span><span class="pln"> optparse</span><span class="pun">.</span><span class="typ">OptionParser</span><span class="pun">(</span><span class="pln">usage</span><span class="pun">=</span><span class="pln">sys</span><span class="pun">.</span><span class="pln">modules</span><span class="pun">[</span><span class="pln">__name__</span><span class="pun">].</span><span class="pln">__doc__</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="40" onclick="window.location.hash='#40'"></td><td class="FileContents-lineContents" id="40"><span class="pln">  _</span><span class="pun">,</span><span class="pln"> args </span><span class="pun">=</span><span class="pln"> parser</span><span class="pun">.</span><span class="pln">parse_args</span><span class="pun">()</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="41" onclick="window.location.hash='#41'"></td><td class="FileContents-lineContents" id="41"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="42" onclick="window.location.hash='#42'"></td><td class="FileContents-lineContents" id="42"><span class="pln">  </span><span class="kwd">if</span><span class="pln"> len</span><span class="pun">(</span><span class="pln">args</span><span class="pun">)</span><span class="pln"> </span><span class="pun">==</span><span class="pln"> </span><span class="lit">0</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="43" onclick="window.location.hash='#43'"></td><td class="FileContents-lineContents" id="43"><span class="pln">    parser</span><span class="pun">.</span><span class="pln">error</span><span class="pun">(</span><span class="str">&#39;Need at least one commit.&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="44" onclick="window.location.hash='#44'"></td><td class="FileContents-lineContents" id="44"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="45" onclick="window.location.hash='#45'"></td><td class="FileContents-lineContents" id="45"><span class="pln">  </span><span class="kwd">for</span><span class="pln"> arg </span><span class="kwd">in</span><span class="pln"> args</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="46" onclick="window.location.hash='#46'"></td><td class="FileContents-lineContents" id="46"><span class="pln">    commit_name </span><span class="pun">=</span><span class="pln"> </span><span class="typ">GetNameForCommit</span><span class="pun">(</span><span class="pln">arg</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="47" onclick="window.location.hash='#47'"></td><td class="FileContents-lineContents" id="47"><span class="pln">    </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> commit_name</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="48" onclick="window.location.hash='#48'"></td><td class="FileContents-lineContents" id="48"><span class="pln">      </span><span class="kwd">print</span><span class="pun">(</span><span class="str">&#39;%s not found&#39;</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> arg</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="49" onclick="window.location.hash='#49'"></td><td class="FileContents-lineContents" id="49"><span class="pln">      </span><span class="kwd">return</span><span class="pln"> </span><span class="lit">1</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="50" onclick="window.location.hash='#50'"></td><td class="FileContents-lineContents" id="50"><span class="pln">    </span><span class="kwd">print</span><span class="pun">(</span><span class="str">&#39;commit %s was:&#39;</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> arg</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="51" onclick="window.location.hash='#51'"></td><td class="FileContents-lineContents" id="51"><span class="pln">    </span><span class="kwd">print</span><span class="pun">(</span><span class="str">&#39;  initially in &#39;</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> commit_name</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="52" onclick="window.location.hash='#52'"></td><td class="FileContents-lineContents" id="52"><span class="pln">    merges </span><span class="pun">=</span><span class="pln"> </span><span class="typ">GetMergesForCommit</span><span class="pun">(</span><span class="pln">arg</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="53" onclick="window.location.hash='#53'"></td><td class="FileContents-lineContents" id="53"><span class="pln">    </span><span class="kwd">for</span><span class="pln"> merge </span><span class="kwd">in</span><span class="pln"> merges</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="54" onclick="window.location.hash='#54'"></td><td class="FileContents-lineContents" id="54"><span class="pln">      </span><span class="kwd">print</span><span class="pun">(</span><span class="str">&#39;  merged to &#39;</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">GetNameForCommit</span><span class="pun">(</span><span class="pln">merge</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">&#39; (as &#39;</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> merge </span><span class="pun">+</span><span class="pln"> </span><span class="str">&#39;)&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="55" onclick="window.location.hash='#55'"></td><td class="FileContents-lineContents" id="55"><span class="pln">    </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> merges</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="56" onclick="window.location.hash='#56'"></td><td class="FileContents-lineContents" id="56"><span class="pln">      </span><span class="kwd">print</span><span class="pun">(</span><span class="str">&#39;No merges found. If this seems wrong, be sure that you did:&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="57" onclick="window.location.hash='#57'"></td><td class="FileContents-lineContents" id="57"><span class="pln">      </span><span class="kwd">print</span><span class="pun">(</span><span class="str">&#39;  git fetch origin &amp;&amp; gclient sync --with_branch_heads&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="58" onclick="window.location.hash='#58'"></td><td class="FileContents-lineContents" id="58"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="59" onclick="window.location.hash='#59'"></td><td class="FileContents-lineContents" id="59"><span class="pln">  </span><span class="kwd">return</span><span class="pln"> </span><span class="lit">0</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="60" onclick="window.location.hash='#60'"></td><td class="FileContents-lineContents" id="60"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="61" onclick="window.location.hash='#61'"></td><td class="FileContents-lineContents" id="61"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="62" onclick="window.location.hash='#62'"></td><td class="FileContents-lineContents" id="62"><span class="kwd">if</span><span class="pln"> __name__ </span><span class="pun">==</span><span class="pln"> </span><span class="str">&#39;__main__&#39;</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="63" onclick="window.location.hash='#63'"></td><td class="FileContents-lineContents" id="63"><span class="pln">  </span><span class="kwd">try</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="64" onclick="window.location.hash='#64'"></td><td class="FileContents-lineContents" id="64"><span class="pln">    sys</span><span class="pun">.</span><span class="pln">exit</span><span class="pun">(</span><span class="pln">main</span><span class="pun">())</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="65" onclick="window.location.hash='#65'"></td><td class="FileContents-lineContents" id="65"><span class="pln">  </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">KeyboardInterrupt</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="66" onclick="window.location.hash='#66'"></td><td class="FileContents-lineContents" id="66"><span class="pln">    sys</span><span class="pun">.</span><span class="pln">stderr</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span><span class="str">&#39;interrupted\n&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="67" onclick="window.location.hash='#67'"></td><td class="FileContents-lineContents" id="67"><span class="pln">    sys</span><span class="pun">.</span><span class="pln">exit</span><span class="pun">(</span><span class="lit">1</span><span class="pun">)</span></td></tr></table></div> <!-- Container --></div> <!-- Site-content --><footer class="Site-footer"><div class="Footer"><span class="Footer-poweredBy">Powered by <a href="https://gerrit.googlesource.com/gitiles/">Gitiles</a>| <a href="https://policies.google.com/privacy">Privacy</a></span><span class="Footer-formats"><a class="u-monospace Footer-formatsItem" href="?format=TEXT">txt</a> <a class="u-monospace Footer-formatsItem" href="?format=JSON">json</a></span></div></footer></body></html>