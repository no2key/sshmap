#Copyright (c) 2010-2015 Yahoo! Inc. All rights reserved.
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. See accompanying LICENSE file.

try:
    import sshmap.sshmap
    import sshmap.callback
    import sshmap.utility
    import sshmap.runner

    # For backwards compatibility
    from sshmap.callback import summarize_failures as \
        callback_summarize_failures
    from sshmap.callback import aggregate_output as callback_aggregate_output
    from sshmap.callback import exec_command as callback_exec_command
    from sshmap.callback import filter_match as callback_filter_match
    from sshmap.callback import status_count as callback_status_count

    # The actual used sshmap functions
    from sshmap.sshmap import run, run_command, run_with_runner
except ImportError:
    import sshmap
    import callback
    import utility
    import runner

    # For backwards compatibility
    from callback import summarize_failures as callback_summarize_failures
    from callback import aggregate_output as callback_aggregate_output
    from callback import exec_command as callback_exec_command
    from callback import filter_match as callback_filter_match
    from callback import status_count as callback_status_count

    # The actual used sshmap functions
    from sshmap import run, run_command, run_with_runner
