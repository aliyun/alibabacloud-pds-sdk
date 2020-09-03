// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * delete share request
     */
    public class DeleteShareRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=true)]
        public string ShareId { get; set; }

    }

}
