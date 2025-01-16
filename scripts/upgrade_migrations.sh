#!/bin/bash

poetry env activate

echo ""
echo "Running migrations..."
echo ""

alembic upgrade head
