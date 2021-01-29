// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class GetAppPublicKeyRequest : TeaModel {
        /// <summary>
        /// App ID
        /// </summary>
        [NameInMap("app_id")]
        [Validation(Required=true)]
        public string AppId { get; set; }

    }

}
