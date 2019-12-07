<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>git_new_branch.py - chromium/tools/depot_tools.git - Git at Google</title><link rel="stylesheet" type="text/css" href="/+static/base.vsKBklzePi_Td7VvkjGVKw.cache.css"><link rel="stylesheet" type="text/css" href="/+static/prettify/prettify.pZ5FqzM6cPxAflH0va2Ucw.cache.css"><!-- default customHeadTagPart --></head><body class="Site"><header class="Site-header"><div class="Header"><a class="Header-image" href="/"><img src="//www.gstatic.com/images/branding/lockups/2x/lockup_git_color_108x24dp.png" width="108" height="24" alt="Google Git"></a><div class="Header-menu"> <a class="Header-menuItem" href="https://accounts.google.com/AccountChooser?service=gerritcodereview&amp;continue=https://chromium.googlesource.com/login/chromium/tools/depot_tools.git/%2B/refs/heads/master/git_new_branch.py">Switch user</a> <a class="Header-menuItem" href="https://chromium.googlesource.com/+logout?continue=/chromium/tools/depot_tools.git/%2B/refs/heads/master/git_new_branch.py">Sign out</a> <span class="Header-menuItem Header-menuItem--noAction">‪pratan niamjoi‬ &lt;tanknug1983@gmail.com&gt;</span> </div></div></header><div class="Site-content"><div class="Container "><div class="Breadcrumbs"><a class="Breadcrumbs-crumb" href="/?format=HTML">chromium</a> / <a class="Breadcrumbs-crumb" href="/chromium/">chromium</a> / <a class="Breadcrumbs-crumb" href="/chromium/tools/">tools</a> / <a class="Breadcrumbs-crumb" href="/chromium/tools/depot_tools.git/">depot_tools.git</a> / <a class="Breadcrumbs-crumb" href="/chromium/tools/depot_tools.git/+/refs/heads/master">refs/heads/master</a> / <a class="Breadcrumbs-crumb" href="/chromium/tools/depot_tools.git/+/refs/heads/master/">.</a> / <span class="Breadcrumbs-crumb">git_new_branch.py</span></div><div class="u-sha1 u-monospace BlobSha1">blob: 856b6eab92261f079fcd9bf82f89715aee26755c [<a href="/chromium/tools/depot_tools.git/+/refs/heads/master/git_new_branch.py">file</a>] [<a href="/chromium/tools/depot_tools.git/+log/refs/heads/master/git_new_branch.py">log</a>] [<a href="/chromium/tools/depot_tools.git/+blame/refs/heads/master/git_new_branch.py">blame</a>]</div><table class="FileContents"><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="1" onclick="window.location.hash='#1'"></td><td class="FileContents-lineContents" id="1"><span class="com">#!/usr/bin/env python</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="2" onclick="window.location.hash='#2'"></td><td class="FileContents-lineContents" id="2"><span class="com"># Copyright 2014 The Chromium Authors. All rights reserved.</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="3" onclick="window.location.hash='#3'"></td><td class="FileContents-lineContents" id="3"><span class="com"># Use of this source code is governed by a BSD-style license that can be</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="4" onclick="window.location.hash='#4'"></td><td class="FileContents-lineContents" id="4"><span class="com"># found in the LICENSE file.</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="5" onclick="window.location.hash='#5'"></td><td class="FileContents-lineContents" id="5"><span class="str">&quot;&quot;&quot;</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="6" onclick="window.location.hash='#6'"></td><td class="FileContents-lineContents" id="6"><span class="str">Create new branch tracking origin/master by default.</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="7" onclick="window.location.hash='#7'"></td><td class="FileContents-lineContents" id="7"><span class="str">&quot;&quot;&quot;</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="8" onclick="window.location.hash='#8'"></td><td class="FileContents-lineContents" id="8"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="9" onclick="window.location.hash='#9'"></td><td class="FileContents-lineContents" id="9"><span class="kwd">import</span><span class="pln"> argparse</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="10" onclick="window.location.hash='#10'"></td><td class="FileContents-lineContents" id="10"><span class="kwd">import</span><span class="pln"> sys</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="11" onclick="window.location.hash='#11'"></td><td class="FileContents-lineContents" id="11"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="12" onclick="window.location.hash='#12'"></td><td class="FileContents-lineContents" id="12"><span class="kwd">import</span><span class="pln"> subprocess2</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="13" onclick="window.location.hash='#13'"></td><td class="FileContents-lineContents" id="13"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="14" onclick="window.location.hash='#14'"></td><td class="FileContents-lineContents" id="14"><span class="kwd">from</span><span class="pln"> git_common </span><span class="kwd">import</span><span class="pln"> run</span><span class="pun">,</span><span class="pln"> root</span><span class="pun">,</span><span class="pln"> set_config</span><span class="pun">,</span><span class="pln"> get_or_create_merge_base</span><span class="pun">,</span><span class="pln"> tags</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="15" onclick="window.location.hash='#15'"></td><td class="FileContents-lineContents" id="15"><span class="kwd">from</span><span class="pln"> git_common </span><span class="kwd">import</span><span class="pln"> hash_one</span><span class="pun">,</span><span class="pln"> upstream</span><span class="pun">,</span><span class="pln"> set_branch_config</span><span class="pun">,</span><span class="pln"> current_branch</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="16" onclick="window.location.hash='#16'"></td><td class="FileContents-lineContents" id="16"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="17" onclick="window.location.hash='#17'"></td><td class="FileContents-lineContents" id="17"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="18" onclick="window.location.hash='#18'"></td><td class="FileContents-lineContents" id="18"><span class="kwd">def</span><span class="pln"> main</span><span class="pun">(</span><span class="pln">args</span><span class="pun">):</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="19" onclick="window.location.hash='#19'"></td><td class="FileContents-lineContents" id="19"><span class="pln">  parser </span><span class="pun">=</span><span class="pln"> argparse</span><span class="pun">.</span><span class="typ">ArgumentParser</span><span class="pun">(</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="20" onclick="window.location.hash='#20'"></td><td class="FileContents-lineContents" id="20"><span class="pln">    formatter_class</span><span class="pun">=</span><span class="pln">argparse</span><span class="pun">.</span><span class="typ">ArgumentDefaultsHelpFormatter</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="21" onclick="window.location.hash='#21'"></td><td class="FileContents-lineContents" id="21"><span class="pln">    description</span><span class="pun">=</span><span class="pln">__doc__</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="22" onclick="window.location.hash='#22'"></td><td class="FileContents-lineContents" id="22"><span class="pln">  </span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="23" onclick="window.location.hash='#23'"></td><td class="FileContents-lineContents" id="23"><span class="pln">  parser</span><span class="pun">.</span><span class="pln">add_argument</span><span class="pun">(</span><span class="str">&#39;branch_name&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="24" onclick="window.location.hash='#24'"></td><td class="FileContents-lineContents" id="24"><span class="pln">  g </span><span class="pun">=</span><span class="pln"> parser</span><span class="pun">.</span><span class="pln">add_mutually_exclusive_group</span><span class="pun">()</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="25" onclick="window.location.hash='#25'"></td><td class="FileContents-lineContents" id="25"><span class="pln">  g</span><span class="pun">.</span><span class="pln">add_argument</span><span class="pun">(</span><span class="str">&#39;--upstream-current&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--upstream_current&#39;</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="26" onclick="window.location.hash='#26'"></td><td class="FileContents-lineContents" id="26"><span class="pln">                 action</span><span class="pun">=</span><span class="str">&#39;store_true&#39;</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="27" onclick="window.location.hash='#27'"></td><td class="FileContents-lineContents" id="27"><span class="pln">                 help</span><span class="pun">=</span><span class="str">&#39;set upstream branch to current branch.&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="28" onclick="window.location.hash='#28'"></td><td class="FileContents-lineContents" id="28"><span class="pln">  g</span><span class="pun">.</span><span class="pln">add_argument</span><span class="pun">(</span><span class="str">&#39;--upstream&#39;</span><span class="pun">,</span><span class="pln"> metavar</span><span class="pun">=</span><span class="str">&#39;REF&#39;</span><span class="pun">,</span><span class="pln"> default</span><span class="pun">=</span><span class="pln">root</span><span class="pun">(),</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="29" onclick="window.location.hash='#29'"></td><td class="FileContents-lineContents" id="29"><span class="pln">                 help</span><span class="pun">=</span><span class="str">&#39;upstream branch (or tag) to track.&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="30" onclick="window.location.hash='#30'"></td><td class="FileContents-lineContents" id="30"><span class="pln">  g</span><span class="pun">.</span><span class="pln">add_argument</span><span class="pun">(</span><span class="str">&#39;--inject-current&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--inject_current&#39;</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="31" onclick="window.location.hash='#31'"></td><td class="FileContents-lineContents" id="31"><span class="pln">                 action</span><span class="pun">=</span><span class="str">&#39;store_true&#39;</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="32" onclick="window.location.hash='#32'"></td><td class="FileContents-lineContents" id="32"><span class="pln">                 help</span><span class="pun">=</span><span class="str">&#39;new branch adopts current branch\&#39;s upstream,&#39;</span><span class="pln"> </span><span class="pun">+</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="33" onclick="window.location.hash='#33'"></td><td class="FileContents-lineContents" id="33"><span class="pln">                 </span><span class="str">&#39; and new branch becomes current branch\&#39;s upstream.&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="34" onclick="window.location.hash='#34'"></td><td class="FileContents-lineContents" id="34"><span class="pln">  g</span><span class="pun">.</span><span class="pln">add_argument</span><span class="pun">(</span><span class="str">&#39;--lkgr&#39;</span><span class="pun">,</span><span class="pln"> action</span><span class="pun">=</span><span class="str">&#39;store_const&#39;</span><span class="pun">,</span><span class="pln"> const</span><span class="pun">=</span><span class="str">&#39;lkgr&#39;</span><span class="pun">,</span><span class="pln"> dest</span><span class="pun">=</span><span class="str">&#39;upstream&#39;</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="35" onclick="window.location.hash='#35'"></td><td class="FileContents-lineContents" id="35"><span class="pln">                 help</span><span class="pun">=</span><span class="str">&#39;set basis ref for new branch to lkgr.&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="36" onclick="window.location.hash='#36'"></td><td class="FileContents-lineContents" id="36"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="37" onclick="window.location.hash='#37'"></td><td class="FileContents-lineContents" id="37"><span class="pln">  opts </span><span class="pun">=</span><span class="pln"> parser</span><span class="pun">.</span><span class="pln">parse_args</span><span class="pun">(</span><span class="pln">args</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="38" onclick="window.location.hash='#38'"></td><td class="FileContents-lineContents" id="38"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="39" onclick="window.location.hash='#39'"></td><td class="FileContents-lineContents" id="39"><span class="pln">  </span><span class="kwd">try</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="40" onclick="window.location.hash='#40'"></td><td class="FileContents-lineContents" id="40"><span class="pln">    </span><span class="kwd">if</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">inject_current</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="41" onclick="window.location.hash='#41'"></td><td class="FileContents-lineContents" id="41"><span class="pln">      below </span><span class="pun">=</span><span class="pln"> current_branch</span><span class="pun">()</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="42" onclick="window.location.hash='#42'"></td><td class="FileContents-lineContents" id="42"><span class="pln">      </span><span class="kwd">if</span><span class="pln"> below </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">None</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="43" onclick="window.location.hash='#43'"></td><td class="FileContents-lineContents" id="43"><span class="pln">        </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">Exception</span><span class="pun">(</span><span class="str">&#39;no current branch&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="44" onclick="window.location.hash='#44'"></td><td class="FileContents-lineContents" id="44"><span class="pln">      above </span><span class="pun">=</span><span class="pln"> upstream</span><span class="pun">(</span><span class="pln">below</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="45" onclick="window.location.hash='#45'"></td><td class="FileContents-lineContents" id="45"><span class="pln">      </span><span class="kwd">if</span><span class="pln"> above </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">None</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="46" onclick="window.location.hash='#46'"></td><td class="FileContents-lineContents" id="46"><span class="pln">        </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">Exception</span><span class="pun">(</span><span class="str">&#39;branch %s has no upstream&#39;</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> </span><span class="pun">(</span><span class="pln">below</span><span class="pun">))</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="47" onclick="window.location.hash='#47'"></td><td class="FileContents-lineContents" id="47"><span class="pln">      run</span><span class="pun">(</span><span class="str">&#39;checkout&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--track&#39;</span><span class="pun">,</span><span class="pln"> above</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;-b&#39;</span><span class="pun">,</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">branch_name</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="48" onclick="window.location.hash='#48'"></td><td class="FileContents-lineContents" id="48"><span class="pln">      run</span><span class="pun">(</span><span class="str">&#39;branch&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--set-upstream-to&#39;</span><span class="pun">,</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">branch_name</span><span class="pun">,</span><span class="pln"> below</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="49" onclick="window.location.hash='#49'"></td><td class="FileContents-lineContents" id="49"><span class="pln">    </span><span class="kwd">elif</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">upstream_current</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="50" onclick="window.location.hash='#50'"></td><td class="FileContents-lineContents" id="50"><span class="pln">      run</span><span class="pun">(</span><span class="str">&#39;checkout&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--track&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;-b&#39;</span><span class="pun">,</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">branch_name</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="51" onclick="window.location.hash='#51'"></td><td class="FileContents-lineContents" id="51"><span class="pln">    </span><span class="kwd">else</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="52" onclick="window.location.hash='#52'"></td><td class="FileContents-lineContents" id="52"><span class="pln">      </span><span class="kwd">if</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">upstream </span><span class="kwd">in</span><span class="pln"> tags</span><span class="pun">():</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="53" onclick="window.location.hash='#53'"></td><td class="FileContents-lineContents" id="53"><span class="pln">        </span><span class="com"># TODO(iannucci): ensure that basis_ref is an ancestor of HEAD?</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="54" onclick="window.location.hash='#54'"></td><td class="FileContents-lineContents" id="54"><span class="pln">        run</span><span class="pun">(</span><span class="str">&#39;checkout&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--no-track&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;-b&#39;</span><span class="pun">,</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">branch_name</span><span class="pun">,</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="55" onclick="window.location.hash='#55'"></td><td class="FileContents-lineContents" id="55"><span class="pln">            hash_one</span><span class="pun">(</span><span class="pln">opts</span><span class="pun">.</span><span class="pln">upstream</span><span class="pun">))</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="56" onclick="window.location.hash='#56'"></td><td class="FileContents-lineContents" id="56"><span class="pln">        set_config</span><span class="pun">(</span><span class="str">&#39;branch.%s.remote&#39;</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">branch_name</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;.&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="57" onclick="window.location.hash='#57'"></td><td class="FileContents-lineContents" id="57"><span class="pln">        set_config</span><span class="pun">(</span><span class="str">&#39;branch.%s.merge&#39;</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">branch_name</span><span class="pun">,</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">upstream</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="58" onclick="window.location.hash='#58'"></td><td class="FileContents-lineContents" id="58"><span class="pln">      </span><span class="kwd">else</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="59" onclick="window.location.hash='#59'"></td><td class="FileContents-lineContents" id="59"><span class="pln">        </span><span class="com"># TODO(iannucci): Detect unclean workdir then stash+pop if we need to</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="60" onclick="window.location.hash='#60'"></td><td class="FileContents-lineContents" id="60"><span class="pln">        </span><span class="com"># teleport to a conflicting portion of history?</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="61" onclick="window.location.hash='#61'"></td><td class="FileContents-lineContents" id="61"><span class="pln">        run</span><span class="pun">(</span><span class="str">&#39;checkout&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;--track&#39;</span><span class="pun">,</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">upstream</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;-b&#39;</span><span class="pun">,</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">branch_name</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="62" onclick="window.location.hash='#62'"></td><td class="FileContents-lineContents" id="62"><span class="pln">    get_or_create_merge_base</span><span class="pun">(</span><span class="pln">opts</span><span class="pun">.</span><span class="pln">branch_name</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="63" onclick="window.location.hash='#63'"></td><td class="FileContents-lineContents" id="63"><span class="pln">  </span><span class="kwd">except</span><span class="pln"> subprocess2</span><span class="pun">.</span><span class="typ">CalledProcessError</span><span class="pln"> </span><span class="kwd">as</span><span class="pln"> cpe</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="64" onclick="window.location.hash='#64'"></td><td class="FileContents-lineContents" id="64"><span class="pln">    sys</span><span class="pun">.</span><span class="pln">stdout</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span><span class="pln">cpe</span><span class="pun">.</span><span class="pln">stdout</span><span class="pun">.</span><span class="pln">decode</span><span class="pun">(</span><span class="str">&#39;utf-8&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;replace&#39;</span><span class="pun">))</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="65" onclick="window.location.hash='#65'"></td><td class="FileContents-lineContents" id="65"><span class="pln">    sys</span><span class="pun">.</span><span class="pln">stderr</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span><span class="pln">cpe</span><span class="pun">.</span><span class="pln">stderr</span><span class="pun">.</span><span class="pln">decode</span><span class="pun">(</span><span class="str">&#39;utf-8&#39;</span><span class="pun">,</span><span class="pln"> </span><span class="str">&#39;replace&#39;</span><span class="pun">))</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="66" onclick="window.location.hash='#66'"></td><td class="FileContents-lineContents" id="66"><span class="pln">    </span><span class="kwd">return</span><span class="pln"> </span><span class="lit">1</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="67" onclick="window.location.hash='#67'"></td><td class="FileContents-lineContents" id="67"><span class="pln">  sys</span><span class="pun">.</span><span class="pln">stderr</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span><span class="str">&#39;Switched to branch %s.\n&#39;</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> opts</span><span class="pun">.</span><span class="pln">branch_name</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="68" onclick="window.location.hash='#68'"></td><td class="FileContents-lineContents" id="68"><span class="pln">  </span><span class="kwd">return</span><span class="pln"> </span><span class="lit">0</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="69" onclick="window.location.hash='#69'"></td><td class="FileContents-lineContents" id="69"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="70" onclick="window.location.hash='#70'"></td><td class="FileContents-lineContents" id="70"></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="71" onclick="window.location.hash='#71'"></td><td class="FileContents-lineContents" id="71"><span class="kwd">if</span><span class="pln"> __name__ </span><span class="pun">==</span><span class="pln"> </span><span class="str">&#39;__main__&#39;</span><span class="pun">:</span><span class="pln">  </span><span class="com"># pragma: no cover</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="72" onclick="window.location.hash='#72'"></td><td class="FileContents-lineContents" id="72"><span class="pln">  </span><span class="kwd">try</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="73" onclick="window.location.hash='#73'"></td><td class="FileContents-lineContents" id="73"><span class="pln">    sys</span><span class="pun">.</span><span class="pln">exit</span><span class="pun">(</span><span class="pln">main</span><span class="pun">(</span><span class="pln">sys</span><span class="pun">.</span><span class="pln">argv</span><span class="pun">[</span><span class="lit">1</span><span class="pun">:]))</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="74" onclick="window.location.hash='#74'"></td><td class="FileContents-lineContents" id="74"><span class="pln">  </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">KeyboardInterrupt</span><span class="pun">:</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="75" onclick="window.location.hash='#75'"></td><td class="FileContents-lineContents" id="75"><span class="pln">    sys</span><span class="pun">.</span><span class="pln">stderr</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span><span class="str">&#39;interrupted\n&#39;</span><span class="pun">)</span></td></tr><tr class="u-pre u-monospace FileContents-line"><td class="u-lineNum u-noSelect FileContents-lineNum" data-line-number="76" onclick="window.location.hash='#76'"></td><td class="FileContents-lineContents" id="76"><span class="pln">    sys</span><span class="pun">.</span><span class="pln">exit</span><span class="pun">(</span><span class="lit">1</span><span class="pun">)</span></td></tr></table></div> <!-- Container --></div> <!-- Site-content --><footer class="Site-footer"><div class="Footer"><span class="Footer-poweredBy">Powered by <a href="https://gerrit.googlesource.com/gitiles/">Gitiles</a>| <a href="https://policies.google.com/privacy">Privacy</a></span><span class="Footer-formats"><a class="u-monospace Footer-formatsItem" href="?format=TEXT">txt</a> <a class="u-monospace Footer-formatsItem" href="?format=JSON">json</a></span></div></footer></body></html>