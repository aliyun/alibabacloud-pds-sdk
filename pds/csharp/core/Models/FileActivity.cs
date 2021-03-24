// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class FileActivity : TeaModel {
        /// <summary>
        /// Actors
        /// </summary>
        [NameInMap("actors")]
        [Validation(Required=false)]
        public List<Actor> Actors { get; set; }

        [NameInMap("primary_action_detail")]
        [Validation(Required=false)]
        public ActionDetail PrimaryActionDetail { get; set; }

        /// <summary>
        /// Targets
        /// </summary>
        [NameInMap("targets")]
        [Validation(Required=false)]
        public List<Target> Targets { get; set; }

        [NameInMap("time_range")]
        [Validation(Required=false)]
        public TimeRange TimeRange { get; set; }

        /// <summary>
        /// Timestamp
        /// </summary>
        [NameInMap("timestamp")]
        [Validation(Required=false)]
        public string Timestamp { get; set; }

    }

}
