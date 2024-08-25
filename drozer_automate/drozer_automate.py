import subprocess
import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <package_name>")
    print(f"\t\t{sys.argv[0]} com.flipkart.android")
    sys.exit(0)

drozer_path = "drozer"

html_result = f"""
<html>
<head>
    <title>Drozer report: {sys.argv[1]}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
        }}
        h1 {{
            background: #333;
            color: #fff;
            padding: 10px 0;
            text-align: center;
            margin: 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        table, th, td {{
            border: 1px solid #ddd;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #4CAF50;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        tr:hover {{
            background-color: #ddd;
        }}
        pre {{
            white-space: pre-wrap; /* Wrap text */
            word-wrap: break-word; /* Break long lines */
            background: #f9f9f9;
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 5px;
        }}
        .separator {{
            border-top: 2px solid #4CAF50;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <h1>Report: {sys.argv[1]}</h1>
"""


def execute_command(test, package_name, package_required=True):
    drozer_cmd = f'{drozer_path} console connect -c "run {test} {package_name}"'
    if not package_required:
        drozer_cmd = f'{drozer_path} console connect -c "run {test} "'
    process = subprocess.Popen(drozer_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    data = output.decode('latin1')
    status = process.wait()
    if "could not find the package" in data:
        data = "Invalid package"
    return data


def process_results(heading, out):
    global html_result
    out = out.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>").replace("\r", "")
    html_result += f"""
    <table>
        <tr>
            <th colspan="2">{heading}</th>
        </tr>
        <tr>
            <td colspan="2">
                <pre>{out}</pre>
            </td>
        </tr>
    </table>
    <div class="separator"></div>
    """


if __name__ == '__main__':
    package_name = sys.argv[1]
    # Get package
    # package_info = execute_command('app.package.info -a', package_name)
    # process_results("Package", package_info)
    # Get attack surface details
    attacksurface_info = execute_command('app.package.attacksurface', package_name)
    process_results("Attack Surface", attacksurface_info)
    # Get activity
    activity_info = execute_command('app.activity.info -i -u -a', package_name)
    process_results("Activities", activity_info)
    # Get broadcast receiver
    broadcast_info = execute_command('app.broadcast.info -i -u -a', package_name)
    process_results("Broadcast Receivers", broadcast_info)
    # Get package with backup API details
    backupapi_info = execute_command('app.package.backup -f', package_name)
    process_results("Package with Backup API", backupapi_info)
    # Get Android Manifest of the package
    # manifest_info = execute_command('app.package.manifest', package_name)
    # process_results("Android Manifest File", manifest_info)
    # Get native libraries
    nativelib_info = execute_command('app.package.native', package_name)
    process_results("Native Libraries used", nativelib_info)
    # Get content provider
    contentprovider_info = execute_command('app.provider.info -u -a', package_name)
    process_results("Content Provider", contentprovider_info)
    # Get URIs from package
    finduri_info = execute_command('app.provider.finduri', package_name)
    process_results("Content Provider URIs", finduri_info)
    # Get services
    services_info = execute_command('app.service.info -i -u -a', package_name)
    process_results("Services", services_info)
    # Get native components included in package
    nativecomponents_info = execute_command('scanner.misc.native -a', package_name)
    process_results("Native Components in Package", nativecomponents_info)
    # Get world readable files in app installation directory /data/data/<package_name>/
    worldreadable_info = execute_command('scanner.misc.readablefiles /data/data/' + package_name + '/', package_name, False)
    process_results("World Readable Files in App Installation Location", worldreadable_info)
    # Get world writable files in app installation directory /data/data/<package_name>/
    worldwriteable_info = execute_command('scanner.misc.readablefiles /data/data/' + package_name + '/', package_name, False)
    process_results("World Writeable Files in App Installation Location", worldwriteable_info)
    # Get content providers that can be queried from current context
    querycp_info = execute_command('scanner.provider.finduris -a', package_name)
    process_results("Content Providers Query from Current Context", querycp_info)
    # Perform SQL Injection on content providers
    sqli_info = execute_command('scanner.provider.injection -a', package_name)
    process_results("SQL Injection on Content Providers", sqli_info)
    # Find SQL Tables trying SQL Injection
    sqltables_info = execute_command('scanner.provider.sqltables -a', package_name)
    process_results("SQL Tables using SQL Injection", sqltables_info)
    # Test for directory traversal vulnerability
    dirtraversal_info = execute_command('scanner.provider.traversal -a', package_name)
    process_results("Directory Traversal using Content Provider", dirtraversal_info)

    html_result += "</body></html>"
    with open(f"report{package_name}.html", "w", encoding="utf-8") as f:
        f.write(html_result)
    print(f"[*] 'report{package_name}.html' with testing results saved")
