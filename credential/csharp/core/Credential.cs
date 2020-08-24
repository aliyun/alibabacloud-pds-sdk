// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

using Tea;
using Tea.Utils;

using AlibabaCloud.AccessTokenCredential.Models;
using System.Net;
using System.Text;
using Newtonsoft.Json;

namespace AlibabaCloud.AccessTokenCredential
{
    public class Credential 
    {
        protected string _endpoint;
        protected string _domainId;
        protected string _clientId;
        protected string _refreshToken;
        protected string _clientSecret;
        protected string _accessToken;
        protected string _expireTime;

        public Credential(Config config)
        {
            this._endpoint = config.Endpoint;
            this._domainId = config.DomainId;
            this._clientId = config.ClientId;
            this._refreshToken = config.RefreshToken;
            this._clientSecret = config.ClientSecret;
            this._accessToken = config.AccessToken;
            this._expireTime = config.ExpireTime;
        }


        public void SetExpireTime(string expireTime)
        {
            this._expireTime = expireTime;
        }

        public string GetExpireTime()
        {
            return _expireTime;
        }

        public string GetRefreshToken()
        {
            return _refreshToken;
        }

        public void SetRefreshToken(string refreshToken)
        {
            this._refreshToken = refreshToken;
        }

        public void SetAccessToken(string accessToken)
        {
            this._accessToken = accessToken;
        }

        public string GetAccessToken()
        {
            if (_accessToken == null || WithShouldRefresh())
            {
                RefreshAccessToken();
            }
            return this._accessToken;
        }

        public async Task<string> GetAccessTokenAsync()
        {
            if (_accessToken == null || WithShouldRefresh())
            {
                await RefreshAccessTokenAsync();
            }
            return this._accessToken;
        }

        internal bool WithShouldRefresh()
        {
            if (string.IsNullOrWhiteSpace(this._refreshToken) || string.IsNullOrWhiteSpace(this._expireTime))
            {
                return false;
            }
            string expireTimeStr = this._expireTime.Replace('T', ' ').Replace('Z', ' ');
            DateTime expireDate = Convert.ToDateTime(expireTimeStr);
            long expireTimeMillis = expireDate.GetTimeMillis();
            return DateTime.UtcNow.GetTimeMillis() >= (expireTimeMillis - 180);
        }

        internal void RefreshAccessToken()
        {
            TeaRequest request = new TeaRequest();
            request.Protocol = "http";
            request.Method = "POST";
            request.Pathname = "/v2/oauth/token";
            request.Headers = new Dictionary<string, string>();
            request.Headers.Add("host", GetHost(this._endpoint, this._domainId + ".api.aliyunpds.com"));
            request.Headers.Add("content-type", "application/x-www-form-urlencoded; charset=utf-8");
            request.Headers.Add("date", TimeUtils.GetGMTDate());
            request.Headers.Add("accept", "application/json");
            request.Headers.Add("x-acs-signature-method", "HMAC-SHA1");
            request.Headers.Add("x-acs-signature-version", "1.0");
            string bodyStr = string.Format("grant_type=refresh_token&refresh_token={0}&client_id={1}&client_secret={2}",
                this._refreshToken, this._clientId, this._clientSecret);
            MemoryStream stream = new MemoryStream();
            byte[] bytes = Encoding.UTF8.GetBytes(bodyStr);
            stream.Write(bytes, 0, bytes.Length);
            request.Body = stream;
            TeaResponse response = TeaCore.DoAction(request, new Dictionary<string, object>());
            string body = TeaCore.GetResponseBody(response);
            Dictionary<string, object> bodyDict = JsonConvert.DeserializeObject<Dictionary<string, object>>(body);
            if (response.StatusCode == 200)
            {
                _expireTime = bodyDict.Get("expire_time").ToSafeString();
                _accessToken = bodyDict.Get("access_token").ToSafeString();
                _refreshToken = bodyDict.Get("refresh_token").ToSafeString();
            }
            else
            {
                throw new WebException("http request is failed.");
            }
        }

        internal async Task RefreshAccessTokenAsync()
        {
            TeaRequest request = new TeaRequest();
            request.Protocol = "http";
            request.Method = "POST";
            request.Pathname = "/v2/oauth/token";
            request.Headers = new Dictionary<string, string>();
            request.Headers.Add("host", GetHost(this._endpoint, this._domainId + ".api.aliyunpds.com"));
            request.Headers.Add("content-type", "application/x-www-form-urlencoded; charset=utf-8");
            request.Headers.Add("date", TimeUtils.GetGMTDate());
            request.Headers.Add("accept", "application/json");
            request.Headers.Add("x-acs-signature-method", "HMAC-SHA1");
            request.Headers.Add("x-acs-signature-version", "1.0");
            string bodyStr = string.Format("grant_type=refresh_token&refresh_token={0}&client_id={1}&client_secret={2}",
                this._refreshToken, this._clientId, this._clientSecret);
            MemoryStream stream = new MemoryStream();
            byte[] bytes = Encoding.UTF8.GetBytes(bodyStr);
            await stream.WriteAsync(bytes, 0, bytes.Length);
            request.Body = stream;
            TeaResponse response = await TeaCore.DoActionAsync(request, new Dictionary<string, object>());
            string body = TeaCore.GetResponseBody(response);
            Dictionary<string, object> bodyDict = JsonConvert.DeserializeObject<Dictionary<string, object>>(body);
            if (response.StatusCode == 200)
            {
                _expireTime = bodyDict.Get("expire_time").ToSafeString();
                _accessToken = bodyDict.Get("access_token").ToSafeString();
                _refreshToken = bodyDict.Get("refresh_token").ToSafeString();
            }
            else
            {
                throw new WebException("http request is failed.");
            }
        }

        internal string GetHost(string endpoint, string domain)
        {
            if (!string.IsNullOrWhiteSpace(endpoint))
            {
                return endpoint;
            }
            else
            {
                return domain;
            }
        }

    }
}
