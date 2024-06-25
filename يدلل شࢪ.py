import requests, os
from user_agent import *
#====الوان====
Z = '\033[1;31m'  # أحمر
F = '\033[2;32m'  # أخضر
B = '\033[2;36m'  # أزرق
W = '\033[0;37m'  # رمادي
m = "\u001b[38;5;15m" #ابيض
#====الوان====
see = input(f' {W} s{B}essioni{W}d : {B}')
rapp = input(f' {W} Enter {B}the video {W}link : ')   
os.system('clear')
headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'ar-US,ar;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'sessionid={see}',
        'origin': 'https://www.instagram.com',
        'referer': f'{rapp}',
        'user-agent': str(generate_user_agent()),
    }
    
data = {
        'container_module': 'reelsTab',
        'entry_point': '1',
        'location': '6',
        'object_id': '3396840407926536557',
        'object_type': '1',
        'context': '{"tags":["ig_self_injury_v3"],"ixt_context_from_www":"QVRNRTVzTGV2UTNwbXZ2MGV1cWZ0R3NnUjBjU3ZpUThtV3NtbjFjRmZKTXc0NzRFWTVxWHpoUHYySzJfREVieWtKV19uWmJOSTJkcU9BLWFVVl9yMEpJSUNtM0htT1BYSmtRelBycms3aVBvTk5qZjVXNEpDV3QtMUNIUmRFYkQ4RnpWQ21WVGJGb2tPa2Y4bHJiRnJvV2xrSjVwc3VUX216UWRLZEFyYnNGeUVzZ2w4bGxnV0dJci1EdjIzNnNwcTBXdUgyejEtWHlOX24yZjdManB3YWJvRVJLLUhoemRoQ3kzMllrcnlzeFg4N283RmJqTVFyb3d4VTVXTGhHLXVEMXMwMXVkT3E4NW5JakwwMWtMbzRuUkRKZ1ZZLVNlWlMzV2lscGhiVk5uRnU2cXNOLUM4dVRQOFNydXdRdVlwbzRTcXk0V0ZNSG1KeXJ2MUFoWWxxX3FoRFc0dHl0elZIX3JMaGN3TWhoMHhDdlFxaFhpa3hKTTNsUXNqd1ZIVm95OWZIUTh5UzVwVWdHS1ZNMFZKaVctUWk1WnJIVUhEUk56NDZXZnF6a3FkbGtqSnVjM0Myc09TYm5JenpIWWJsb2ktYkp4QWRhejNJeWE1UzltbDl1R19NYkxaYlNGYUZpdnY2bDdmbnIyUmVlMWRGbVA5OHZUd2F1NUJsREZWakJNMTBIbzd1RDNuTWtkQkpER2FMdURFeXVTVkpyVnhwWWVGMXUwVXA2dmFEQ1JhNVI4UC1NT2tsbnJNSi1UYldPN281MHBYdUlJeVZnSkFwbnMtQVVzVHdTTnhoYWFjZENpZWUzM1pjY3ppZUI5c214VFpSdUlVZGVQZmRWU2c4ZmFUQUFidXpfQU9pM3FwT0pGM0x4UjBOS3ZkR3dXUmE3bTU1QnJmaW5YeGtleHlWUFhIQzF2RUowU0pIaGRNMG5WbFdTdm5CdFpqM2hidHg2Mm9KakJUbEMtUlFJM2Rtd3YtbEhZanlqTXRYQkhlSVh6ZVVWX1M4ekwxWjJoSElMcXdPVFFIc0IxblJ1U3ZNZHlaa2lTZ0Q3TjRKeVdCUDExWHlQTExfRnlIeFM0eU1QSUd0N1pNUFM5SzRIVnZFQjNUNE5EWWdZcnFIbi1WWFBCSkQtOUFya3BXSDdNekxoeVBRRUNlYUlueHZZdUVmdm5OSDN0UllDZXZUUnFUUVpvcDZEa1VWcGY4YU44cVdNVGlSbG5oQjRfblJTelJDTXdaZHVkbTNCMmVHdE81VGdnaGdoRjJ3QVM5N1l6SThfM2tSQWhPTFJETGZOY1ZDRHBzSWhBRzUyVmkyb3ZFTVZsMXJGRURLOXhvMElycG5XMEtqQTQ2ak8xWmh0azhDVVZOZE80QWdRakVUaVU5S1JJZnlOZlI1QVc1VzZXZmwtaldGQ29BeEJVUVplY1ZJSE10VnlUejVYQWUyVy1JN0VMMDZhd2tCRklTNW5qX2dzZnZvX0Z1YWNnMG16RUlYaUNLS05yX19La1JUczlnNERpaFh3TWFnMHpScF8zRjJ6YW1xTnVid1VPTDVUbkxjR055N3BkZHRRSjRYUWtZRGFzXzlFUEtCNDBaV2hWUjRMVTNBZkt6U1pTcDRHQVRBRk41cWFyVExsdmtPZjNTTUYxX2lEamRiWHlWeGc4bk5ZOENwclBLdFo3Q2Y3Z2REUWRvOHowSERvSUotaEdFUlJuSWlRLWFvcWhRM3NXV0V6Snh5MkVINlVmNnVpT2syWUxQMnNmZHViVjdHZXFVOE1meVBMMlJUdXpMS2JpdXZvQWRuN3dla3NxbWdBX0MtVWxiLXdQaVJ5OXhyaHJpLVNXekNiTUhLUUlTNjZDb1p2azF4SzNRNmk0QXFoWXBpX0RKN0hDSEUzVGxyVjBQNE9aNVZYUWxiOTlhWUJaUk00QXFRWWJpU0IyZnE1SUxnbnpCZ3FUazVwd1NUVkxNbUwwc2JDbzhCbXZsUXN3b2g4Nld6SlN5VHN2MXJweGlqVW0wQWFRVkIta2Y5QWM1M193YW5yeWwwLW1QVU1fcFdZS3c4X3J4NGdWdDRlTVpfZF9FQzNPLUI1Ul9wanNwY08tRGwwN0ZVd0UtYTNuU3V1OTZ1LWF5NUtTNElQR29od1F2RFg3WjVIZU5RUHlzZHZySkpDbnNlZ1hiRmNpYXBNV2RLSTBCdUF6enlvT3NkRlpYNlprWkZVZmJvZXpfNHI4bDJXQ0d0ZTF3U29ySkVmRHBTV0hmeF9BZ0hTWS00R2l1RFlta3B6dFpmbGItVk0wYVZ1TDBqVXVGeTV2N1FwcFhRQXdTVDRydURZLUFZcDEtaE1TWFZEVElEc25QRXFSeHFvS1g4b2p4cWdQRVh3SG14R2JicW5WbkswYVF6VnNPVUFrRk9CYmtFVmpTZWtNaU51eDBqanpDVUEweE1EQmx3Mk1YVG8tT0hNRVNCQXVEc1NXNXZDU25OallvRzN3dlNidDl5eU1aU0Zja05WWDRHZWVjazViVS1CNl9sdlZrVVhFeVlMVENnTmJHOGpZSUFJSkEyc0JWU0x3NWJHQVZOTmxMR0E1YmlUUjAxczloQ0dibFhIZ1k4d0ttOXQ0ZDVDV3djajNLWGRtaTBHM2RRRk9rT1R5S3hTNktfLVp5bkdwejR4QThvejdFUEF3Q2NOeVVwNlRVWWxLcEpZR3ZGdEhYeDdQdmMwUkQxRl95QW9kRF9uZ2ZQazh4OWcxajFXUHgzbHQ4eUd2c3A0aWRDX1lJc3Z5V2ZWcWJjTllUZHYxZGxvazI1d3NyeHhXZU9xYzFMaU5yX3VJSE9HOUx5Zmo4dVRyUS0tNHA2MUpfV2MwZXN3M2ZwMGtQVlJfUGlRQkthNmZ1d01GaHlNdUZJSkJMMGxyb3BVQ2VWc1FqRUZNWGRhMVl3amZ2WU1ncVdyLTBmSTBrVVk4MUVCSDhYLTJuUy1jcVNyV0JnUWxybFc0X01reF85QTVfSUdkMTgzTlRyRWh1dHg0UmU5UGpzVWhXTHhUM2J5QzJjb0NITkQ2bmdJTFAtU2N2dDF6QVRBeVFTTDhtbERuRlBLRWNhcmxGemc3aDJ6clBKS3FNM1VsOFdqWm5pcWdNOFZpSnlSdEdyY3h1U09zM2QtbFh2cm9yX3pnQkFuaTNiRkF6TXRmUTloRTBCclVkRzNKTlpUekVFV2kwMjQxRHpRLWtiRVd3b3djRXRfV1M1d3lCaFRFRmd4TzR4OHlaS2ZLcjA0MW5BQUJJQUpud3ZvYmhxRHp6ak5vWWlrYUxrYWNPT29uWUU2X1E5UldndnlPLU1WaS1hYU55c1JzMnYtdjJjbmdHWTg2LWdNSEhHdlk1VEtGNkIxQWZHaUttNGdSTTFmc1J4d0t3OWtidWFZcUxVTWJCYldSeTJ2NTY2dzZ0Z3cwWTZ1a2xyYUljUjJkYzUybjAzM1A5VVRjV1ZvUFRuVm44SWV2NnFhX3RHNFVjTHpiSkdsLU5KN1BkRlFSLXAtc0hZVDFtdVRIOVdfamg3VEJJZy00OE5fNzVfYVA3ZElGNUtoSHFVVlpDM2FLZVV6Z1lmOFVKaVNreUcyM1pjYjJFOUVIbDlmcXlhZU1iOXNIRXd0NTAwYVdZSUY1X0RFQm13ZXNNYTctbjUxZ0FLeXFzT3J2amNvbGlzSmIyWTFUdW1hajdpX0tyTEh4c2JVNlRabkJKTWtmdk5Ca3d6bVB0M2hpNWZHMjlqZ3lxeS1CZDd1WERtd1lCOTVHVFZpeTNBVWdGWTNvX0VoY0ppR2d0SEVmVTFhMzQ5dkZyelpGNDVnVVpjWVAtZ2JsSERLNGNKVi03ZDd4eFVLbTI1ZE9ZdTNLSlZqd1UtTW9DNUg5S0pfUTJaNm1WZW5SYi01VEJTZy1iN2NpdWc=","frx_context_from_www":"{\\"location\\":\\"ig_post\\",\\"entry_point\\":\\"chevron_button\\",\\"session_id\\":\\"507814f0-1f6e-425e-9d4a-e18be3be8763\\",\\"tags\\":[\\"ig_self_injury_v3\\"],\\"object\\":\\"{\\\\\\"media_id\\\\\\":\\\\\\"3396840407926536557\\\\\\"}\\",\\"reporter_id\\":17841401156504155,\\"responsible_id\\":17841430483432773,\\"locale\\":\\"ar_AR\\",\\"app_platform\\":4,\\"extra_data\\":{\\"container_module\\":\\"reelsTab\\",\\"app_version\\":\\"None\\",\\"is_dark_mode\\":null,\\"app_id\\":936619743392459,\\"sentry_feature_map\\":\\"JqzS0f0BGA0zNy4yMzcuMTIwLjE1GGVNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjQuMC4wLjAgU2FmYXJpLzUzNy4zNhgFYXJfQVIcGCBjNWQwM2U4OGY0YWE3NGEyZGNjMDEwZWU1ZjEwYjNmYhgAGCAxZTA1MDZlODFhZjNmNDNmZGIxMzYwYmVjNzA0ZDAzYRgkcXVpYzAwOWExNTkwYTE2ZWIxZTkwNjEwMTAyYzRhMzUzOWFlFZznGCggYWIxNjJiN2VjNWRjZWQ2YmQ1NzEyYmFiNzA4YzhlNGEAPCwYHFpuWmpKZ0FFQUFFNFZxWklXYlpPYlZsRl9zQTIW4LGa54dkABwVCCsBiAJvcwNYMTEAIjw5FQAZFQA5FQAAGCBjNTE2YWRkMWZkY2Y0ODBjODY3MTM4ZTUyOTBmMzdiNhUCERIYDzkzNjYxOTc0MzM5MjQ1ORwW0qeB2Kyjtz8YQDAxNzA0NjcwZmY5Nzc1YTEyZGIyMzlmMjRlYTA4ODY0ZmRhMWFkM2QyOGZjZTBhYmVlODFjZDRhYjI3YzhhZTQAHBUEABIoLGh0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vcmVlbHMvQzhrQUZxUkozbHQvGA5YTUxIdHRwUmVxdWVzdAAWtqnUo52qsT8oIy9hcGkvdjEvd2ViL3JlcG9ydHMvZ2V0X2ZyeF9wcm9tcHQvFi4WqNi55wwA\\",\\"shopping_session_id\\":null,\\"logging_extra\\":null,\\"is_in_holdout\\":null,\\"preloading_enabled\\":null},\\"frx_feedback_submitted\\":false,\\"ufo_key\\":\\"ufo-6bb3a7d4-a44f-4831-99a9-86fafd085e9b\\",\\"additional_data\\":{\\"is_ixt_session\\":true,\\"frx_validation_ent\\":\\"IGEntMedia\\"},\\"profile_search\\":false,\\"screen_type\\":\\"frx_policy_education\\"}"}',
        'action_type': '2',
        'frx_prompt_request_type': '4',
    }
while True:
    try:
        re = requests.post(
            'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',
            headers=headers,
            data=data,
        ).text
        if '"message":"CSRF token missing or incorrect"' in re:
            print(f'{F} The video has been reported{m} | {F} تم التبليغ')
        else:
            print(f'{Z} an error occurred {m}| {Z} حدث خطاء')    
    except:
        print('Erorr')   
        exec()         
