#!/bin/bash

### Custom deploy step triggered on after_success
###
### For libs, pushes eggs.
### For apps, push to Aptible.

# Fail on error
set -e
# Fail on syntax errors
bash -n "$0"


echo 'Starting deploy.'

if [ ${TRAVIS_PULL_REQUEST} != 'false' ]; then
    echo 'Build triggered by pull request; do not deploy.'
    exit 0
fi


### Egg

echo 'Starting sdist build.'

if [ ${TRAVIS_BRANCH} == 'master' ] || \
   [ ${TRAVIS_BRANCH} == 'develop' ]; then
    echo 'Branch is master or develop; no extra version tags.'
    EGG_INFO='egg_info -R -D'
else
    echo 'Branch is not master or develop; extra version tags.'
    TAG=${TRAVIS_BRANCH}_$(git log -1 --format='%h')
    echo "Extra version tags are '${TAG}'."
    EGG_INFO="egg_info -R -D -b ${TAG}"
fi

python setup.py ${EGG_INFO} sdist

echo 'sdist build succeeded.'


echo 'Starting Gemfury push'

FULL_NAME=$(python setup.py --fullname)
echo "Package is '${FULL_NAME}'."

FILE_PATH=./dist/${FULL_NAME}.tar.gz

curl -f -F package=@${FILE_PATH} https://${GEMFURY_API_TOKEN}@push.fury.io/cloverhealth/

echo 'Gemfury push succeeded.'


# Done!
echo 'Deploy succeeded.'
exit 0
