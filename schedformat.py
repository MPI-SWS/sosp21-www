#!/usr/bin/env python3

f = open("program.md","r")

for l in f:
    if l.startswith("TITLE "):
        print("          <tr><td>")
        print("            <span class=\"pull-right\">")
        print("              <a href=\"#\"><img class=\"icon-paper\" src=\"images/icon-paper.png\"></img></a>")
        print("              <a href=\"#\"><img class=\"icon-slide\" src=\"images/icon-slide.png\"></img></a>")
        print("              <a href=\"#\"><img class=\"icon-video\" src=\"images/icon-video.png\"></img></a>")
        print("              <a href=\"#\"><img class=\"icon-minutes\" src=\"images/icon-minutes.png\"></img></a>")
        print("              <a href=\"#\"><img class=\"icon-links\" src=\"images/icon-links.png\"></img></a>")
        print("              <a href=\"#\"><img class=\"icon-answer\" src=\"images/icon-answer.png\"></img></a>")
        print("            </span>")
        print("            <strong><a href=\"\">" + l[6:] + "</a></strong>")
        print("          </td></tr>")
    if l.startswith("AUTHORS "):
        print("          <tr><td>" + l[8:] + "</td></tr>")
