# frozen_string_literal: true

# This file is used by Rack-based servers to start the application.

require_relative './server'
application = HelloWorld.new

run(application)
