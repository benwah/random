require 'rack'
require 'net/http'
require 'json'

class HelloWorld
  ENDPOINT = URI(ENV['REMOTE_ENDPOINT'])

  def call(env)
    [ 200, { "Content-Type" => "text/plain" }, [fetch_remote_data] ]
  end

  def fetch_remote_data
    JSON.parse(
      Net::HTTP.get(ENDPOINT)
    )[0]['guid']
  end
end
