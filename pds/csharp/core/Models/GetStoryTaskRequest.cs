// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * Get create story task request
     */
    public class GetStoryTaskRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// Drive ID
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=true)]
        public string DriveId { get; set; }

    }

}
