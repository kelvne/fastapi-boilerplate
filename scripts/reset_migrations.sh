#!/bin/bash

poetry env activate

echo ""
echo "Resetting migrations..."
echo ""

alembic downgrade base
