###############################################################################
Build
###############################################################################

:term:`OpenNMT` の :term:`Lua` 実装のDockerバージョンを利用する。

Install
###############################################################################

Docker
===============================================================================

Dockerhubのイメージは、　Dockerfileを比べる限り :term:`SentencePiece`
のインストール が含まれていないため、github
リポジトリのDockerfileを利用して、Dockerイメージ をBuildする。 

#. :term:`OpenNMT` リポジトリのクローン

   .. code-block:: console
   
      $ cd ${repo_root}
      $ git clone https://github.com/OpenNMT/OpenNMT.git

#. Docker build

   .. code-block:: console

      $ cd OpenNMT
      $ sudo docker build . -t opennmt/opennmt:latest


   .. note:: 私の利用した環境 [#localenv]_ では、5時間ほどかかった


Configuration
###############################################################################


Docker Compose
===============================================================================

サービス単位で構成して簡単に使いたいため、Docker Composeを利用する。

.. literalinclude:: ../../docker-compose.yml
   :language: yml
   :caption: Docker Compose構成ファイル


.. [#localenv] - MacBook
               - NTT光
               - so-net
