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
    public class ImageTagResponse : TeaModel {
        /// <summary>
        /// 聚类标签计数
        /// </summary>
        [NameInMap("count")]
        [Validation(Required=false)]
        public long Count { get; set; }

        /// <summary>
        /// cover_file_id
        /// </summary>
        [NameInMap("cover_file_id")]
        [Validation(Required=false)]
        public string CoverFileId { get; set; }

        /// <summary>
        /// 聚类标签封面图片地址
        /// </summary>
        [NameInMap("cover_url")]
        [Validation(Required=false)]
        public string CoverUrl { get; set; }

        /// <summary>
        /// 聚类标签名称
        /// </summary>
        [NameInMap("name")]
        [Validation(Required=false)]
        public string Name { get; set; }

    }

}
