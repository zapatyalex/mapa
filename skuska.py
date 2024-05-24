import gpxpy

def parse_gpx(gpx_file):
    with open(gpx_file, 'r') as f:
        gpx = gpxpy.parse(f)
    
    
    print(f"Creator: {gpx.creator}")
    print(f"Version: {gpx.version}")



    for track in gpx.tracks:
        print(f"Jazda: {track.name}")
        for segment in track.segments:
            for point in segment.points:
                print(f"Miesto ({point.latitude}, {point.longitude})")
                print(f"Vyska: {point.elevation}")
                print(f"Cas: {point.time}\n")
             


gpx_file = 'F:/Trip_2024-05-21_ebike-connect-1.gpx'
parse_gpx(gpx_file)
