// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * Get drive request
     */
    public class GetDriveRequest : TeaModel {
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
