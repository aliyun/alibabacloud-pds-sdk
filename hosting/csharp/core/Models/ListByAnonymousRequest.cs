// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * list_file_by_anonymous request
     */
    public class ListByAnonymousRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// image_thumbnail_process
        /// </summary>
        [NameInMap("image_thumbnail_process")]
        [Validation(Required=false)]
        public string ImageThumbnailProcess { get; set; }

        /// <summary>
        /// image_url_process
        /// </summary>
        [NameInMap("image_url_process")]
        [Validation(Required=false)]
        public string ImageUrlProcess { get; set; }

        /// <summary>
        /// limit
        /// </summary>
        [NameInMap("limit")]
        [Validation(Required=false)]
        public long? Limit { get; set; }

        /// <summary>
        /// marker
        /// </summary>
        [NameInMap("marker")]
        [Validation(Required=false)]
        public string Marker { get; set; }

        /// <summary>
        /// parent_file_id
        /// </summary>
        [NameInMap("parent_file_id")]
        [Validation(Required=true, MaxLength=50, Pattern="[a-z0-9]{1,50}")]
        public string ParentFileId { get; set; }

        [NameInMap("referer")]
        [Validation(Required=false)]
        public string Referer { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=true)]
        public string ShareId { get; set; }

        [NameInMap("sign_token")]
        [Validation(Required=false)]
        public string SignToken { get; set; }

        /// <summary>
        /// video_thumbnail_process
        /// type:string
        /// </summary>
        [NameInMap("video_thumbnail_process")]
        [Validation(Required=false)]
        public string VideoThumbnailProcess { get; set; }

    }

}
