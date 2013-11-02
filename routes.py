from flask import Flask, jsonify

app = Flask(__name__) 

@app.route('/', methods = ['GET', 'POST'])
def resume():
  name = ['Faye Purdum']
  email = ['fayepurdum@gmail.com']
  phone = ['360.556.2690']
  location = ['Portland, OR, 97206']
  portfolio_link = ['fayeishere.github.com']
  summary = ['My history is steeped in resourcefulness, productivity and efficiency. My future is brewing with resourceful technology and entertainment.']
  skills = ['Ruby, Sinatra, Rack, Rails, Python, Flask, PHP, HTML5, CSS3, Bootstrap, Middleman, Jekyll, SQL, Redis, Javascript, AJAX, jQuery, APIs, Git, Agile, Unix']
  experience = (0, ['Social API Intern @ Wieden+Kennedy in Portland, OR during Aug, 2013 to Present', ['Social API Engineer Intern. HTTP APIs, REST clients and reverse engineering. Rapid prototyping environments in JS, Python, PHP. Digital strategy and user behaviour. Facebook Open Graph API, Login/Connect and JS SDK, Permissions paradigm and policies.', ['Dodge Durango - Ron Burgundy YouTube gadget with customized interruptions and email form. (Built/Deployed) http://www.youtube.com/user/dodge/durango', 'Social networking app (unreleased) - PSD to HTML/CSS', 'W+K Pie Eating Contest Fundraising Website with Paypal Integration, IPN listener, Redis (Full Stack PHP)', 'Various prototype API mashups in Python and node.js']]], 1, ['Student @ Portland Code School in Portland, OR during Jan, 2013 to May, 2013', ['Creating web applications utilizing skills and methods while contributing to the GitHub open source environment.', ['Freecycle Mapper: Freecycle google map mashup built in Sinatra with jQuery. Migrated to Rails.', 'CAHW: A class project app - users vote for Cards Against Humanity choices, showing winning pairs for the ultimate war of words experience.', 'Pre-kix: An app for Kickstarter users to organize and prepare for their upcoming projects - and beyond!']]], 2, ['Founder @ Be a Tree Productions in Portland, OR during Jan, 2011 to Present', ['Writing, directing, audio recording, post production, editing, publishing and marketing of an audio play series, Flint Lock Investigations. http://flintlockinvestigations.tumblr.com']], 3, ['Pricing Task Force @ Powell\'s Books in Portland, OR during Mar, 2010 to Jan, 2013', ['Pricing books, receiving and assessing orders through the online buyback program, processing, fulfilling orders, data entry, transferring items.']])
  education = (0, ['Portland Code School', ['Intensive 12-week web development program, 2013']], 1, ['Evergreen State College', ['Bachelor or Arts, Community Development, 2009']])
  community = (0, ['Coders With Kids', ['Co-Organizer, 2013']], 1, ['Feral Cat Coalition of Oregon, Portland', ['Clinic Volunteer, 2009/2010']], 2, ['Terra Commons, Olympia, WA', ['Edible Forest Garden Intern, 2009']])
  resume = [
        {
            "name": name,
            "email": email,
            "phone": phone,
            "location": location,
            "portfolio_link": portfolio_link,
            "summary": summary,
            "skills": skills,
            "experience": experience,
            "education": education,
            "community": community,
        }
  ]

  return jsonify( { "resume": resume})


if __name__ == '__main__':
  app.run(debug=True)