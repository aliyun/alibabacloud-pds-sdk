// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * List file response
     */
    public class OSSListFileResponse : TeaModel {
        /// <summary>
        /// items
        /// </summary>
        [NameInMap("items")]
        [Validation(Required=false)]
        public List<BaseOSSFileResponse> Items { get; set; }

        /// <summary>
        /// next_marker
        /// </summary>
        [NameInMap("next_marker")]
        [Validation(Required=false)]
        public string NextMarker { get; set; }

    }

}
