// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 获取download url response
     */
    public class GetDownloadUrlResponse : TeaModel {
        /// <summary>
        /// expiration
        /// </summary>
        [NameInMap("expiration")]
        [Validation(Required=false)]
        public string Expiration { get; set; }

        /// <summary>
        /// method
        /// </summary>
        [NameInMap("method")]
        [Validation(Required=false)]
        public string Method { get; set; }

        [NameInMap("ratelimit")]
        [Validation(Required=false)]
        public RateLimit Ratelimit { get; set; }

        /// <summary>
        /// size
        /// </summary>
        [NameInMap("size")]
        [Validation(Required=false)]
        public long Size { get; set; }

        /// <summary>
        /// streams url info
        /// </summary>
        [NameInMap("streams_url")]
        [Validation(Required=false)]
        public Dictionary<string, object> StreamsUrl { get; set; }

        /// <summary>
        /// url
        /// </summary>
        [NameInMap("url")]
        [Validation(Required=false)]
        public string Url { get; set; }

    }

}
