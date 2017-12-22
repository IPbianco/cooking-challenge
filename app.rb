ENV['RACK_ENV'] ||= 'development'
require 'sinatra/base'
require 'json'

class Cooking < Sinatra::Base

  enable :sessions

  get '/' do
    erb(:index)
  end

  post '/' do
    File.open("data/user_ingredients.json","w") do |f|
      f.write(params.to_json)
    end
    result = `python3 source/user_ingredients.py`
    session[:prediction] = result
    redirect '/prediction'
  end

  get '/prediction' do
    content_type :json
    { prediction: session[:prediction] }.to_json
  end

  get '/ingredients' do
    content_type :json
    ingredients = `python3 source/ingredients_list.py`
    ingredients = ingredients.split("', '")
    ingredients.shift
    ingredients.pop
    { ingredients: ingredients }.to_json
  end

  run! if app_file == $0
end
