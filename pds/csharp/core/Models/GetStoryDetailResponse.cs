// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 故事详情
     */
    public class GetStoryDetailResponse : TeaModel {
        /// <summary>
        /// cover_file_id
        /// </summary>
        [NameInMap("cover_file_id")]
        [Validation(Required=false)]
        public string CoverFileId { get; set; }

        /// <summary>
        /// created_at
        /// </summary>
        [NameInMap("created_at")]
        [Validation(Required=false)]
        public string CreatedAt { get; set; }

        /// <summary>
        /// items
        /// </summary>
        [NameInMap("items")]
        [Validation(Required=false)]
        public List<BaseFileResponse> Items { get; set; }

        /// <summary>
        /// score
        /// </summary>
        [NameInMap("score")]
        [Validation(Required=false)]
        public double? Score { get; set; }

        /// <summary>
        /// story_id
        /// </summary>
        [NameInMap("story_id")]
        [Validation(Required=false)]
        public string StoryId { get; set; }

        /// <summary>
        /// story_images_date_range
        /// </summary>
        [NameInMap("story_images_date_range")]
        [Validation(Required=false)]
        public List<int?> StoryImagesDateRange { get; set; }

        /// <summary>
        /// sub_title
        /// </summary>
        [NameInMap("sub_title")]
        [Validation(Required=false)]
        public string SubTitle { get; set; }

        /// <summary>
        /// title
        /// </summary>
        [NameInMap("title")]
        [Validation(Required=false)]
        public string Title { get; set; }

        /// <summary>
        /// updated_at
        /// </summary>
        [NameInMap("updated_at")]
        [Validation(Required=false)]
        public string UpdatedAt { get; set; }

        /// <summary>
        /// video_status
        /// </summary>
        [NameInMap("video_status")]
        [Validation(Required=false)]
        public string VideoStatus { get; set; }

        /// <summary>
        /// video_url
        /// </summary>
        [NameInMap("video_url")]
        [Validation(Required=false)]
        public string VideoUrl { get; set; }

    }

}
