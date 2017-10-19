from flask import Flask, Response

app = Flask(__name__)
@app.route('/')
def index():
    return """
<!DOCTYPE html>
<html>
<head>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script type="text/javascript">
$(function() {
  var $result = $("#result");
  $("#clear").on('click', function(event) {
    $result.val("");
  });
  $("#plain-text-file").on('click', function(event) {
    $.ajax({
      url: "/plain.json",
      method: "GET",
      dataType: "json",
      success: function(data, status, jqxhr) {
        $result.val(data.data.join(", "));
      }
    });
  });
  $("#gzipped-file").on('click', function(event) {
    $.ajax({
      url: "/gzipped.json",
      method: "GET",
      dataType: "json",
      success: function(data, status, jqxhr) {
        $result.val(data.data.join(", "));
      }
    });
  });
});
</script>
</head>
<body>
<button id="clear">clear</button>
<button id="plain-text-file">plain text file</button>
<button id="gzipped-file">gzipped file</button>
<button id="gzipped-in-postgres">gzipped in postgres</button>
<br/>
<textarea id="result"></textarea>
</body>
</html>
"""

@app.route("/plain.json")
def plain():
    with open("nums.json") as f:
        return Response(f.read(), mimetype="application/json")

@app.route("/gzipped.json")
def gzipped():
    with open("nums.json.gz", "rb") as f:
        r = Response(f.read(), mimetype="application/json")
        r.headers.set("Content-Encoding", "gzip")
        return r

app.run(debug=True)
